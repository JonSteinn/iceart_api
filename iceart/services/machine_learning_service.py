import abc

import cv2
import numpy as np
from flask_caching import Cache
from PIL import Image

from ..models import ImageViewModel, PaintingDto, PaintingViewModel
from ..repositories import IPaintingRepository
from ..utils import (
    CacheKeyManager,
    create_image_hash,
    crop_image,
    get_image_path,
    get_most_difference,
)


class IMachineLearningService(abc.ABC):
    """Interface for painting service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_most_similar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        """Find the most similar image and return its id."""


class MachineLearningService(IMachineLearningService):
    """Machine learning service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, painting_repository: IPaintingRepository, cache: Cache):
        self._painting_repository = painting_repository
        self._cache: Cache = cache

    def _all_hash(self):
        """Return hash for all paintings and cache if necessary"""
        cache_key = CacheKeyManager.ml_cache_key()
        answer: dict = self._cache.get(cache_key)
        if answer is None:
            answer = dict()
            for painting in self._painting_repository.get_all_paintings():
                img = Image.open(get_image_path(painting.file).as_posix())
                answer[painting.identity()] = create_image_hash(img)
            self._cache.set(cache_key, answer)
        return answer

    def get_most_similar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        """Return most similar painting"""
        im_arr = np.frombuffer(image_vm.image, dtype=np.uint8)
        image = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        hash_image = create_image_hash(Image.fromarray(crop_image(image)))
        best = -1
        best_value = get_most_difference()
        hash_list = self._all_hash()
        for k, h in hash_list:
            if best_value > np.count_nonzero(h != hash_image):
                best = k
        fake_vm = PaintingViewModel(best)
        return PaintingDto(self._painting_repository.get_painting_by_id(fake_vm))
