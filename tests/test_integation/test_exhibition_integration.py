import json

from ..mocks.mock_app import MockApp


def test_exhibition_integration_get_all_nearby_exhibitions_ok():
    # Arrange
    app = MockApp()
    my_pos = (64.142634, -21.927622)

    # Act
    res = app.make_post_request(
        "/exhibition", json.dumps({"latitude": my_pos[0], "longitude": my_pos[1]})
    )

    # Assert
    assert res.status_code == 200
    assert json.loads(res.get_data(as_text=True)) == {
        "exhibitions": [
            {
                "id": 1,
                "title": "m_title1",
                "info": "m_info1",
                "latitude": 64.145265,
                "longitude": -21.945307,
            },
            {
                "id": 2,
                "title": "m_title2",
                "info": "m_info2",
                "latitude": 64.15046,
                "longitude": -21.950737,
            },
        ]
    }


def test_exhibition_integration_get_all_nearby_exhibitions_no_lat():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/exhibition", json.dumps({"longitude": 0.0}))

    # Assert
    assert res.status_code == 400


def test_exhibition_integration_get_all_nearby_exhibitions_no_lon():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request("/exhibition", json.dumps({"latitude": 0.0}))

    # Assert
    assert res.status_code == 400


def test_exhibition_integration_get_all_nearby_exhibitions_invalid_lat_type():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request(
        "/exhibition", json.dumps({"latitude": False, "longitude": 0.0})
    )

    # Assert
    assert res.status_code == 400


def test_exhibition_integration_get_all_nearby_exhibitions_invalid_lon_type():
    # Arrange
    app = MockApp()

    # Act
    res = app.make_post_request(
        "/exhibition", json.dumps({"latitude": 0.0, "longitude": {}})
    )

    # Assert
    assert res.status_code == 400
