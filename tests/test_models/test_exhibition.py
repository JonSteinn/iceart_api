import pytest
from werkzeug.exceptions import BadRequest

from iceart.models import Exhibition, ExhibitionDto, ExhibitionsDto, ExhibitionViewModel


def test_exhibition():
    # Arrange
    data = {"_id": 1130, "title": "t", "info": "i", "latitude": 0.75, "longitude": 0.5}

    # Act
    ex = Exhibition(data)

    # Assert
    assert ex.identity == 1130
    assert ex.title == "t"
    assert ex.info == "i"
    assert ex.latitude == 0.75
    assert ex.longitude == 0.5


def test_exhibition_vm_no_lat():
    with pytest.raises(BadRequest):
        vm = ExhibitionViewModel({"longitude": 2.5})


def test_exhibition_vm_no_lon():
    with pytest.raises(BadRequest):
        vm = ExhibitionViewModel({"latitude": "1.5", "longitude": 2.5})


def test_exhibition_vm_invalid_lat_type():
    with pytest.raises(BadRequest):
        vm = ExhibitionViewModel({"latitude": 1.5})


def test_exhibition_vm_invalid_lon_type():
    with pytest.raises(BadRequest):
        vm = ExhibitionViewModel({"latitude": 1.5, "longitude": "2.5"})


def test_exhibition_vm_valid():
    vm = ExhibitionViewModel({"latitude": 1.5, "longitude": 2.5})


def test_exhibition_dto():
    # Arrange
    data = {"_id": 1130, "title": "t", "info": "i", "latitude": 0.75, "longitude": 0.5}
    ex = Exhibition(data)

    # Act
    dto = ExhibitionDto(ex)

    # Assert
    assert dto.as_json() == {
        "id": 1130,
        "title": "t",
        "info": "i",
        "latitude": 0.75,
        "longitude": 0.5,
    }


def test_exhibitions_dto():
    # Arrange
    data = (
        {"_id": 1, "title": "t1", "info": "i1", "latitude": 0.75, "longitude": 0.5},
        {"_id": 2, "title": "t2", "info": "i2", "latitude": 1.75, "longitude": 1.5},
        {"_id": 3, "title": "t3", "info": "i3", "latitude": 2.75, "longitude": 2.5},
    )

    # Act
    dto = ExhibitionsDto((ExhibitionDto(Exhibition(d)) for d in data))

    # Assert
    assert dto.as_json() == {
        "exhibitions": [
            {"id": 1, "title": "t1", "info": "i1", "latitude": 0.75, "longitude": 0.5},
            {"id": 2, "title": "t2", "info": "i2", "latitude": 1.75, "longitude": 1.5},
            {"id": 3, "title": "t3", "info": "i3", "latitude": 2.75, "longitude": 2.5},
        ]
    }
