import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest_mock

from iceart.services import PaintingService

from ..mocks.mock_repositories import MockPaintingRepository
from ..mocks.mock_services import MockMachineLearningService


def test_painting_service_get_painting_by_id():
    # Arrange
    _id = 4
    service = PaintingService(MockPaintingRepository(), MockMachineLearningService())
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xff")
        p = Path(tmp_file.name)

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        response = service.get_painting_by_id(_id)

    # Assert
    assert response.id == _id
    assert response.title == "m_title"
    assert response.info == "m_info"
    assert response.image == "/w=="

    # Cleanup
    os.remove(p)


def test_painting_service_get_akin_painting():
    # Arrange
    service = PaintingService(MockPaintingRepository(), MockMachineLearningService())

    # Act
    painting = service.get_akin_painting({"img": "/w=="})

    # Assert
    assert painting.id == 5
    assert painting.title == "t"
    assert painting.info == "i"
    assert painting.image == "img"
