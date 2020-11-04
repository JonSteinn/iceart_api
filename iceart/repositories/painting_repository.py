import abc
from typing import List

from flask_caching import Cache
from flask_pymongo.wrappers import Database

from ..models import Painting, PaintingViewModel
from ..utils import CacheKeyManager


class IPaintingRepository(abc.ABC):
    """Interface for painting service."""

    @abc.abstractmethod
    def get_painting_by_id(self, painting_vm: PaintingViewModel) -> Painting:
        """Find painting by its id."""

    @abc.abstractmethod
    def get_all_paintings(self) -> List[Painting]:
        """Get all paintings."""


class PaintingRepository(IPaintingRepository):
    """Painting service."""

    def __init__(self, db: Database, cache: Cache):
        self._db: Database = db
        self._cache: Cache = cache

    def get_painting_by_id(self, painting_vm: PaintingViewModel) -> Painting:
        cache_key = CacheKeyManager.painting_id_cache_key(painting_vm.identity)
        answer: dict = self._cache.get(cache_key)
        if answer is None:
            answer = self._db.painting.find_one_or_404(painting_vm.search_key())
            self._cache.set(cache_key, answer)
        return Painting(answer)

    def get_all_paintings(self) -> List[Painting]:
        return [Painting(p) for p in self._db.painting.find()]
