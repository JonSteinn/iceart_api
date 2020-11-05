import abc

import cv2
import numpy as np

from ..models import ImageViewModel, PaintingDto, PaintingViewModel
from ..repositories import IPaintingRepository
from ..utils import create_image_hash, crop_image, get_most_difference, get_image_path


class IMachineLearningService(abc.ABC):
    """Interface for painting service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_most_similar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        """Find the most similar image and return its id."""


class MachineLearningService(IMachineLearningService):
    """Machine learning service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, painting_repository: IPaintingRepository):
        self._painting_repository = painting_repository
        self.HASH_SIZE = 128
        self.MOST_DIFF = self.HASH_SIZE * self.HASH_SIZE
        self.hash_list = dict()

        for p in self._painting_repository.get_all_paintings():
            img = cv2.imread(get_image_path(p.file))
            self.hash_list[p._id] = create_image_hash(img)

    def get_most_similar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        image = crop_image(image_vm.image)
        hash_image = create_image_hash(image)
        best = -1
        best_value = get_most_difference()
        for p in self.hash_list:
            if best_value > np.count_nonzero(self.hash_list[p] != hash_image):
                best = p
        fake_vm = PaintingViewModel(best)
        return PaintingDto(self._painting_repository.get_painting_by_id(fake_vm))
