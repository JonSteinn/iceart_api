import pytest

from iceart.models import ImageViewModel
from iceart.services import MachineLearningService

from ..mocks.mock_repositories import MockPaintingRepository


def test_placeholder():
    ml_service = MachineLearningService(MockPaintingRepository())
    with pytest.raises(NotImplementedError):
        ml_service.get_most_similar_painting(ImageViewModel({"image": "abc=="}))
        # Hey! while you are at it, test me?
