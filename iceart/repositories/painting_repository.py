import abc


class IPaintingRepository(abc.ABC):  # pylint: disable=too-few-public-methods
    """Interface for painting service."""

    @abc.abstractmethod
    def get_user_by_id(self, user_id: int) -> dict:
        """Find user by its id."""


class PaintingRepository(IPaintingRepository):  # pylint: disable=too-few-public-methods
    """Painting service."""

    def __init__(self, db=None):
        self._db = db

    def get_user_by_id(self, user_id: int) -> dict:
        return {"id": user_id}
