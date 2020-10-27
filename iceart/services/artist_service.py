import abc

from ..models import ArtistDto, ArtistViewModel
from ..repositories import IArtistRepository


class IArtistService(abc.ABC):
    """Interface for painting service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_artist_by_id(self, artist_id: int) -> ArtistDto:
        """Find artist by his id."""


class ArtistService(IArtistService):
    """Painting service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, artist_repository: IArtistRepository):
        self._artist_repository = artist_repository

    def get_artist_by_id(self, artist_id: int) -> ArtistDto:
        """Find artist by his id."""
        model = ArtistViewModel(artist_id)
        artist = self._artist_repository.get_artist_by_id(model)
        return ArtistDto(artist)
