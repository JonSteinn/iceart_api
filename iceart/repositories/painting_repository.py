import abc

from flask_pymongo.wrappers import Database


class IPaintingRepository(abc.ABC):  # pylint: disable=too-few-public-methods
    """Interface for painting service."""

    @abc.abstractmethod
    def get_painting_by_id(self, painting_id: int) -> dict:
        """Find user by its id."""


class PaintingRepository(IPaintingRepository):  # pylint: disable=too-few-public-methods
    """Painting service."""

    def __init__(self, db: Database):
        self._db: Database = db

    def get_painting_by_id(self, painting_id: int) -> dict:
        return {"id": painting_id}
