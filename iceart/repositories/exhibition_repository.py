import abc
from typing import List

from flask_caching import Cache
from flask_pymongo.wrappers import Database

from ..models import Exhibition
from ..utils import CacheKeyManager


class IExhibitionRepository(abc.ABC):
    """Interface for exhibition service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_all_exhibitions(self) -> List[Exhibition]:
        """Get all exhibitions."""


class ExhibitionRepository(IExhibitionRepository):
    """Exhibition service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, db: Database, cache: Cache):
        self._db: Database = db
        self._cache: Cache = cache

    def get_all_exhibitions(self) -> List[Exhibition]:
        cache_key = CacheKeyManager.exhibitions_cache_key()
        answer: List[Exhibition] = self._cache.get(cache_key)
        if answer is None:
            answer = [Exhibition(e) for e in self._db.exhibition.find()]
            self._cache.set(cache_key, answer)
        return answer
