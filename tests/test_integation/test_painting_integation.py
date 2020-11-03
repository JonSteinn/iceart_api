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
        "technique": "m_technique2",
        "image": "rw==",
        "year": 2019,
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


def test_painting_integration_upload_invalid_type():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", "notjson")

    # Assert
    assert res.status_code == 400


def test_painting_integration_upload_missing_field():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", json.dumps({"not_img": "x"}))

    # Assert
    assert res.status_code == 400


def test_painting_integration_upload_invalid_field_type():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", json.dumps({"image": 5}))

    # Assert
    assert res.status_code == 400


def test_painting_integration_upload_invalid_img_str_chars():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", json.dumps({"image": "æ"}))

    # Assert
    assert res.status_code == 400


def test_painting_integration_upload_invalid_img_str_padding():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", json.dumps({"image": "x"}))

    # Assert
    assert res.status_code == 400


def test_painting_integration_upload_ok():
    # Hi
    # I'm a placeholder
    # Please implement me when ready
    # Thanks

    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/painting", json.dumps({"image": "af=="}))

    # Assert
    assert res.status_code == 500
