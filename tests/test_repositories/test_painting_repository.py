from iceart.repositories import PaintingRepository

from ..mocks.mock_database import MockDatabase


def test_painting_repository():
    # Arrange
    _id = 4
    repo = PaintingRepository(MockDatabase())
    expected = {"_id": _id, "title": "m_title", "info": "m_info"}

    # Act
    response = repo.get_painting_by_id(4)

    # Assert
    assert response == expected
