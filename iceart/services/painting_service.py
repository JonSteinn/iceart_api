import abc

from ..repositories import IPaintingRepository


class IPaintingService(abc.ABC):  # pylint: disable=too-few-public-methods
    """Interface for painting service."""

    @abc.abstractmethod
    def get_painting_by_id(self, painting_id: int) -> dict:
        """Find user by its id."""


class PaintingService(IPaintingService):  # pylint: disable=too-few-public-methods
    """Painting service."""

    def __init__(self, painting_repository: IPaintingRepository):
        self._painting_repository = painting_repository

    def get_painting_by_id(self, painting_id: int) -> dict:
        return self._painting_repository.get_painting_by_id(painting_id)
