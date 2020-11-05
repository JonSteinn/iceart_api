import pytest
from werkzeug.exceptions import NotFound

from iceart.models import PaintingViewModel
from iceart.repositories import PaintingRepository

from ..mocks.mock_cache import MockCache
from ..mocks.mock_database import MockDatabase


def test_painting_repository_get_painting_by_id_success():
    # Arrange
    _id = 7
    vm = PaintingViewModel(_id)
    repo = PaintingRepository(MockDatabase(), MockCache())

    # Act
    response = repo.get_painting_by_id(vm)
    cached_response = repo.get_painting_by_id(vm)

    # Assert
    assert response.identity == _id
    assert response.title == "m_title7"
    assert response.technique == "m_technique7"
    assert response.artist_id == 2
    assert response.file == "f133.jpg"
    assert response.year == -1
    assert cached_response.identity == _id
    assert cached_response.title == "m_title7"
    assert cached_response.technique == "m_technique7"
    assert cached_response.artist_id == 2
    assert cached_response.file == "f133.jpg"
    assert cached_response.year == -1


def test_painting_repository_get_painting_by_id_not_found():
    # Arrange
    _id = 2222
    repo = PaintingRepository(MockDatabase(), MockCache())
    vm = PaintingViewModel(_id)

    # Act
    with pytest.raises(NotFound):
        repo.get_painting_by_id(vm)

    # Assert


def test_painting_repository_get_all_paintings():
    # Arrange
    repo = PaintingRepository(MockDatabase(), MockCache())

    # Act
    allSorted = sorted(repo.get_all_paintings(), key=lambda p: p.identity)

    # Assert
    assert [p.identity for p in allSorted] == [0, 2, 7]


def test_painting_repository_get_all_paintings_by_ids():
    # Arrange
    repo = PaintingRepository(MockDatabase(), MockCache())

    # Act
    multiple = repo.get_paintings_by_ids([0, 7])
    cached = repo.get_paintings_by_ids([0, 7])

    # Assert
    assert {p.identity for p in multiple} == {0, 7}
    assert {p.identity for p in cached} == {0, 7}
