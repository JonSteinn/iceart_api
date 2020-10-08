from iceart.controllers import PaintingController

from ..mocks.mock_services import MockPaintingService


def test_painting_controller_get_painting_by_id():
    # Arrange
    _id = 4
    controller = PaintingController(MockPaintingService())
    expected = {"_id": _id, "title": "m_title", "info": "m_info"}

    # Act
    response = controller.get_painting_by_id(_id)

    # Assert
    assert response == expected
