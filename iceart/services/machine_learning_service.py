import abc

from flask_caching import Cache

from ..models import ImageViewModel, PaintingDto, PaintingViewModel
from ..repositories import IPaintingRepository
from ..utils import (
    CacheKeyManager,
    create_image_hash_from_bytes,
    create_image_hash_from_file,
    get_image_hash_difference,
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

    def get_most_similar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        """Return most similar painting"""
        v_m = PaintingViewModel(self._get_best_match(image_vm.image))
        return PaintingDto(self._painting_repository.get_painting_by_id(v_m))

    def _get_best_match(self, image: bytes) -> int:
        hash_image = create_image_hash_from_bytes(image)
        best_id, best_value = -1, get_most_difference()
        hash_list = self._all_hash()
        for image_id, image_hash in hash_list.items():
            curr_val = get_image_hash_difference(image_hash, hash_image)
            if best_value > curr_val:
                best_id, best_value = image_id, curr_val
        return best_id

    def _all_hash(self) -> dict:
        """Return hash for all paintings and cache if necessary"""
        cache_key = CacheKeyManager.ml_cache_key()
        answer: dict = self._cache.get(cache_key)
        if answer is None:
            answer = {
                painting.identity: create_image_hash_from_file(painting.file)
                for painting in self._painting_repository.get_all_paintings()
            }
            self._cache.set(cache_key, answer)
        return answer
