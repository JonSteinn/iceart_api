import abc

from ..models import ImageViewModel, PaintingDto, PaintingViewModel
from ..repositories import IPaintingRepository
from .machine_learning_service import IMachineLearningService


class IPaintingService(abc.ABC):
    """Interface for painting service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_painting_by_id(self, painting_id: int) -> PaintingDto:
        """Find artist by its id."""

    @abc.abstractmethod
    def get_akin_painting(self, data: dict) -> PaintingDto:
        """Find the most similar painting."""


class PaintingService(IPaintingService):
    """Painting service."""

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        painting_repository: IPaintingRepository,
        ml_service: IMachineLearningService,
    ):
        self._painting_repository: IPaintingRepository = painting_repository
        self._ml_service: IMachineLearningService = ml_service

    def get_painting_by_id(self, painting_id: int) -> PaintingDto:
        model = PaintingViewModel(painting_id)
        painting = self._painting_repository.get_painting_by_id(model)
        return PaintingDto(painting)

    def get_akin_painting(self, data: dict) -> PaintingDto:
        model = ImageViewModel(data)
        return self._ml_service.get_most_similar_painting(model)
