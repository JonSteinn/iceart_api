import pytest

from iceart.models import ImageViewModel
from iceart.services import MachineLearningService

from ..mocks.mock_cache import MockCache
from ..mocks.mock_repositories import MockPaintingRepository


def test_placeholder():
    ml_service = MachineLearningService(MockPaintingRepository(), MockCache())
    assert True
