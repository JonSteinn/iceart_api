import abc
from typing import List

from flask_pymongo.wrappers import Database

from ..models import Painting, PaintingViewModel


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

    def __init__(self, db: Database):
        self._db: Database = db

    def get_painting_by_id(self, painting_vm: PaintingViewModel) -> Painting:
        answer: dict = self._db.painting.find_one_or_404(painting_vm.search_key())
        return Painting(answer)

    def get_all_paintings(self) -> List[Painting]:
        return [Painting(p) for p in self._db.painting.find()]
