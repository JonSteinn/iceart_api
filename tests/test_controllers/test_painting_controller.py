from iceart.controllers import PaintingController

from ..mocks.mock_services import MockPaintingService


def test_painting_controller_init():
    # Arrange
    _id = 4
    controller = PaintingController(MockPaintingService())
    expected = {"_id": _id, "title": "m_title", "info": "m_info"}

    # Act
    response = controller.get_painting_by_id(4)

    # Assert
    assert response == expected
