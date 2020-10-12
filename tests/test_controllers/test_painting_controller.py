import flask

from iceart.controllers import PaintingController

from ..mocks.mock_services import MockPaintingService


def test_painting_controller_get_painting_by_id():
    # Arrange
    _id = 4
    controller = PaintingController(MockPaintingService())

    # Act
    response = controller.get_painting_by_id(_id)

    # Assert
    assert response == {"id": 5, "title": "t", "info": "i", "image": "img"}


def test_painting_controller_upload_painting():
    # Arrange
    controller = PaintingController(MockPaintingService())

    # Act
    with flask.Flask(__name__).test_request_context():
        response = controller.upload_painting()

    # Assert
    assert response == {"id": 5, "title": "t", "info": "i", "image": "img"}
