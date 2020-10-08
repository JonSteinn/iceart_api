import pytest
from werkzeug.exceptions import NotFound

from iceart.repositories import PaintingRepository

from ..mocks.mock_database import MockDatabase


def test_painting_repository_get_painting_by_id_success():
    # Arrange
    _id = 7
    repo = PaintingRepository(MockDatabase())
    expected = {"_id": _id, "title": "m_title7", "info": "m_info7"}

    # Act
    response = repo.get_painting_by_id(_id)

    # Assert
    assert response == expected


def test_painting_repository_get_painting_by_id_not_found():
    # Arrange
    _id = 2222
    repo = PaintingRepository(MockDatabase())

    # Act
    with pytest.raises(NotFound):
        repo.get_painting_by_id(_id)

    # Assert
