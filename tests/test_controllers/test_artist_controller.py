from iceart.controllers import ArtistController

from ..mocks.mock_services import MockArtistService


def test_painting_controller_get_painting_by_id():
    # Arrange
    _id = 4
    controller = ArtistController(MockArtistService())

    # Act
    response = controller.get_artist_by_id(_id)

    # Assert
    assert response == {"id": 665, "title": "t", "info": "i", "image": "img"}
