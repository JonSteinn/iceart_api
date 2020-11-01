import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest_mock

from iceart.services import ArtistService

from ..mocks.mock_repositories import MockArtistRepository


def test_artist_service_get_artist_by_id():
    # Arrange
    _id = 22
    service = ArtistService(MockArtistRepository())
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xff")
        p = Path(tmp_file.name)

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        response = service.get_artist_by_id(_id)

    # Assert
    assert response.id == _id
    assert response.title == "t"
    assert response.info == "i"
    assert response.image == "/w=="

    # Cleanup
    os.remove(p)
