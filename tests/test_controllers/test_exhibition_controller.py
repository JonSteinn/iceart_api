import flask

from iceart.controllers import ExhibitionController

from ..mocks.mock_services import MockExhibitionService


def test_exhibition_controller_get_all_nearby_exhibitions():
    # Arrange
    controller = ExhibitionController(MockExhibitionService())

    # Act
    with flask.Flask(__name__).test_request_context():
        response = controller.get_all_nearby_exhibitions()

    # Assert
    assert response == {
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
