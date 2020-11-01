import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest_mock

from ..mocks.mock_app import MockApp


def test_artist_integration_get_artist_by_id_ok():
    # Arrange
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xaf")
        p = Path(tmp_file.name)
    app = MockApp()
    _id = 2

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        res = app.make_get_request(f"/artist/{_id}")

    # Assert
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert json.loads(res.get_data(as_text=True)) == {
        "id": 2,
        "title": "ma_title2",
        "info": "ma_info2",
        "image": "rw==",
    }

    # Cleanup
    os.remove(p)


def test_artist_integration_get_artist_by_id_not_found():
    # Arrange
    app = MockApp()
    _id = 1223123

    # Act
    res = app.make_get_request(f"/artist/{_id}")

    # Assert
    assert res.status_code == 404
    assert res.headers["Content-Type"] == "application/json"
