import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest_mock

from iceart.services import ArtistService

from ..mocks.mock_cache import MockCache
from ..mocks.mock_repositories import MockArtistRepository, MockPaintingRepository


def test_artist_service_get_artist_by_id():
    # Arrange
    _id = 22
    service = ArtistService(
        MockArtistRepository(), MockPaintingRepository(), MockCache()
    )
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xff")
        p = Path(tmp_file.name)

    class M:
        def tostring(self):
            return b"\xff\xd8"

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        with pytest_mock.mock.patch("cv2.imread", return_value=None):
            with pytest_mock.mock.patch("cv2.resize", return_value=None):
                with pytest_mock.mock.patch("cv2.imencode", return_value=(None, M())):
                    response = service.get_artist_by_id(_id)

    # Assert
    assert response.id == _id
    assert response.title == "t"
    assert response.info == "i"
    assert response.image == "/w=="
    assert response.paintings == [
        {"id": 4, "image": "/9g="},
        {"id": 77, "image": "/9g="},
    ]

    # Cleanup
    os.remove(p)
