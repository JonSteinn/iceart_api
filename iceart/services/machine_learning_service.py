import abc

from ..models import ImageViewModel, PaintingDto
from ..repositories import IPaintingRepository


class IMachineLearningService(abc.ABC):
    """Interface for painting service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_most_smilar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        """Find the most similar image and return its id."""


class MachineLearningService(IMachineLearningService):
    """Machine learning service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, painting_repository: IPaintingRepository):
        self._painting_repository = painting_repository

    def get_most_smilar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        print("get_most_smilar_painting has not been implemented!", flush=True)
        raise NotImplementedError()
