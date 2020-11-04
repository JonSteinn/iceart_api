import abc

from flask_caching import Cache
from flask_pymongo.wrappers import Database

from ..models import Artist, ArtistViewModel
from ..utils import CacheKeyManager


class IArtistRepository(abc.ABC):
    """Interface for artist service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_artist_by_id(self, artist_vm: ArtistViewModel) -> Artist:
        """Find user by its id."""


class ArtistRepository(IArtistRepository):
    """Artist service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, db: Database, cache: Cache):
        self._db: Database = db
        self._cache: Cache = cache

    def get_artist_by_id(self, artist_vm: ArtistViewModel) -> Artist:
        cache_key = CacheKeyManager.artist_id_cache_key(artist_vm.identity)
        answer: dict = self._cache.get(cache_key)
        if answer is None:
            answer = self._db.artist.find_one_or_404(artist_vm.search_key())
            self._cache.set(cache_key, answer)
        return Artist(answer)
