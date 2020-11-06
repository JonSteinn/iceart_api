import abc

from flask_caching import Cache

from ..models import ArtistDto, ArtistViewModel
from ..repositories import IArtistRepository, IPaintingRepository
from ..utils import CacheKeyManager, get_image_as_thumbnail, get_image_path


class IArtistService(abc.ABC):
    """Interface for artist service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_artist_by_id(self, artist_id: int) -> ArtistDto:
        """Find artist by his id."""


class ArtistService(IArtistService):
    """Artist service."""

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        artist_repository: IArtistRepository,
        painting_repository: IPaintingRepository,
        cache: Cache,
    ):
        self._artist_repository = artist_repository
        self._painting_repository = painting_repository
        self._cache = cache

    def get_artist_by_id(self, artist_id: int) -> ArtistDto:
        """Find artist by his id."""
        cache_key = CacheKeyManager.artist_paintings_cache_key(artist_id)
        answer: ArtistDto = self._cache.get(cache_key)
        if answer is None:
            model = ArtistViewModel(artist_id)
            artist = self._artist_repository.get_artist_by_id(model)
            paintings = self._painting_repository.get_paintings_by_ids(artist.paintings)
            thumbnails = [
                {
                    "id": painting.identity,
                    "image": get_image_as_thumbnail(
                        get_image_path(painting.file).as_posix()
                    ),
                    "name": painting.title,
                }
                for painting in paintings
            ]
            answer = ArtistDto(artist, thumbnails)
            self._cache.set(cache_key, answer)
        return answer
