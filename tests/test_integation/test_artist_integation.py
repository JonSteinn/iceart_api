import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest_mock

from ..mocks.mock_app import MockApp


def test_painting_integration_get_painting_by_id_ok():
    # Arrange
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xaf")
        p = Path(tmp_file.name)
    app = MockApp()
    _id = 2

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        res = app.make_get_request(f"/painting/{_id}")

    # Assert
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert json.loads(res.get_data(as_text=True)) == {
        "id": 2,
        "title": "m_title2",
        "info": "m_info2",
        "image": "rw==",
    }

    # Cleanup
    os.remove(p)


def test_painting_integration_get_painting_by_id_not_found():
    # Arrange
    app = MockApp()
    _id = 4444

    # Act
    res = app.make_get_request(f"/painting/{_id}")

    # Assert
    assert res.status_code == 404
    assert res.headers["Content-Type"] == "application/json"
