import pytest
from werkzeug.exceptions import BadRequest

from iceart.services import ExhibitionService

from ..mocks.mock_repositories import MockExhibitionRepository


def test_get_all_nearby_exhibitions_success():
    # Arrange
    serv = ExhibitionService(MockExhibitionRepository())
    my_pos = (64.142634, -21.927622)
    data = {"latitude": my_pos[0], "longitude": my_pos[1]}

    # Act
    dto = serv.get_all_nearby_exhibitions(data)
    ids = tuple(sorted(x.id for x in dto.exhibitions))

    # Assert
    assert ids == (1, 2)


def test_get_all_nearby_exhibitions_from_antarctica():
    # Arrange
    serv = ExhibitionService(MockExhibitionRepository())
    my_pos = (-85.250759, 71.008255)  # antarctica
    data = {"latitude": my_pos[0], "longitude": my_pos[1]}

    # Act
    dto = serv.get_all_nearby_exhibitions(data)
    ids = tuple(sorted(x.id for x in dto.exhibitions))

    # Assert
    assert ids == ()


def test_get_all_nearby_exhibitions_invalid_model():
    serv = ExhibitionService(MockExhibitionRepository())
    with pytest.raises(BadRequest):
        serv.get_all_nearby_exhibitions({"longitude": 0})
    with pytest.raises(BadRequest):
        serv.get_all_nearby_exhibitions({"latitude": 0})
    with pytest.raises(BadRequest):
        serv.get_all_nearby_exhibitions({"latitude": "X", "longitude": 0})
    with pytest.raises(BadRequest):
        serv.get_all_nearby_exhibitions({"latitude": 0, "longitude": []})
