import pytest
from werkzeug.exceptions import NotFound

from iceart.models import ArtistViewModel
from iceart.repositories import ArtistRepository

from ..mocks.mock_cache import MockCache
from ..mocks.mock_database import MockDatabase


def test_artist_repository_get_artist_by_id_success():
    # Arrange
    _id = 1
    vm = ArtistViewModel(_id)
    repo = ArtistRepository(MockDatabase(), MockCache())

    # Act
    response = repo.get_artist_by_id(vm)
    cached_response = repo.get_artist_by_id(vm)

    # Assert
    assert response.identity == _id
    assert response.title == "ma_title1"
    assert response.info == "ma_info1"
    assert response.file == "rrr.jpg"
    assert response.paintings == [0, 2]
    assert cached_response.identity == _id
    assert cached_response.title == "ma_title1"
    assert cached_response.info == "ma_info1"
    assert cached_response.file == "rrr.jpg"
    assert cached_response.paintings == [0, 2]


def test_artist_repository_get_artist_by_id_not_found():
    # Arrange
    _id = 5135
    vm = ArtistViewModel(_id)
    repo = ArtistRepository(MockDatabase(), MockCache())

    # Act
    # Assert
    with pytest.raises(NotFound):
        repo.get_artist_by_id(vm)
