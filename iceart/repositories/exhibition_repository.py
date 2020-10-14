import abc
from typing import List

from flask_pymongo.wrappers import Database

from ..models import Exhibition


class IExhibitionRepository(abc.ABC):
    """Interface for exhibition service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_all_exhibitions(self) -> List[Exhibition]:
        """Get all exhibitions."""


class ExhibitionRepository(IExhibitionRepository):
    """Exhibition service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, db: Database):
        self._db: Database = db

    def get_all_exhibitions(self) -> List[Exhibition]:
        return [Exhibition(e) for e in self._db.exhibition.find()]
