from iceart.services import PaintingService

from ..mocks.mock_repositories import MockPaintingRepository


def test_painting_service_get_painting_by_id():
    # Arrange
    _id = 4
    service = PaintingService(MockPaintingRepository())
    expected = {"_id": _id, "title": "m_title", "info": "m_info"}

    # Act
    response = service.get_painting_by_id(_id)

    # Assert
    assert response == expected
