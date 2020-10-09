import json

from ..mocks.mock_app import MockApp


def test_painting_integration_get_painting_by_id_ok():
    # Arrange
    app = MockApp()
    _id = 2
    expected = {"_id": _id, "title": "m_title2", "info": "m_info2"}

    # Act
    res = app.make_get_request(f"/painting/{_id}")

    # Assert
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert json.loads(res.get_data(as_text=True)) == expected


def test_painting_integration_get_painting_by_id_not_found():
    # Arrange
    app = MockApp()
    _id = 4444

    # Act
    res = app.make_get_request(f"/painting/{_id}")

    # Assert
    assert res.status_code == 404
    assert res.headers["Content-Type"] == "application/json"
