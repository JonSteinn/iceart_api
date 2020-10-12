import pytest
from werkzeug.exceptions import NotFound

from iceart.models import PaintingViewModel
from iceart.repositories import PaintingRepository

from ..mocks.mock_database import MockDatabase


def test_painting_repository_get_painting_by_id_success():
    # Arrange
    _id = 7
    vm = PaintingViewModel(_id)
    repo = PaintingRepository(MockDatabase())

    # Act
    response = repo.get_painting_by_id(vm)

    # Assert
    assert response.identity == _id
    assert response.title == "m_title7"
    assert response.info == "m_info7"
    assert response.artist_id == 2
    assert response.file == "f133.jpg"


def test_painting_repository_get_painting_by_id_not_found():
    # Arrange
    _id = 2222
    repo = PaintingRepository(MockDatabase())
    vm = PaintingViewModel(_id)

    # Act
    with pytest.raises(NotFound):
        repo.get_painting_by_id(vm)

    # Assert


def test_painting_repository_get_all_paintings():
    # Arrange
    repo = PaintingRepository(MockDatabase())

    # Act
    allSorted = sorted(repo.get_all_paintings(), key=lambda p: p.identity)

    # Assert
    assert [p.identity for p in allSorted] == [0, 2, 7]
