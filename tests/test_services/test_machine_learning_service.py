import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest
import pytest_mock
from _pytest.monkeypatch import MonkeyPatch

from iceart.models import ImageViewModel
from iceart.services import MachineLearningService
from iceart.utils import image_util

from ..mocks.mock_cache import MockCache
from ..mocks.mock_repositories import MockPaintingRepository


def m_create_image_hash_from_bytes(b):
    return [0, 1, 0]


def m_get_most_difference():
    return 4


def m_get_image_hash_difference(h1, h2):
    return sum(x != y for x, y in zip(h1, h2))


def m_create_image_hash_from_file(fn):
    if fn[-1] == "4":
        return [0, 1, 1]
    return [1, 0, 0]


def test_placeholder():
    # Arrange
    mp = MonkeyPatch()
    model = ImageViewModel({"image": "/9j4=="})
    ml_service = MachineLearningService(MockPaintingRepository(), MockCache())
    mp.setattr(
        "iceart.utils.image_util.create_image_hash_from_bytes",
        m_create_image_hash_from_bytes,
    )
    mp.setattr("iceart.utils.image_util.get_most_difference", m_get_most_difference)
    mp.setattr(
        "iceart.utils.image_util.get_image_hash_difference", m_get_image_hash_difference
    )
    mp.setattr(
        "iceart.utils.image_util.create_image_hash_from_file",
        m_create_image_hash_from_file,
    )
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xff")
        p = Path(tmp_file.name)

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        pdto = ml_service.get_most_similar_painting(model)
        pdto_cached = ml_service.get_most_similar_painting(model)

    # Assert
    assert pdto.id == 4
    assert pdto_cached.id == 4

    # Cleanup
    os.remove(p)
