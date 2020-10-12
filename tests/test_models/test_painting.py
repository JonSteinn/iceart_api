import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest
import pytest_mock
from werkzeug.exceptions import NotFound

from iceart.models import Painting, PaintingDto, PaintingViewModel


def test_painting_vm_init():
    with pytest.raises(NotFound):
        PaintingViewModel(-1)


def test_painting_vm_search_key():
    assert PaintingViewModel(3).search_key() == {"_id": 3}


def test_painting_init():
    # Arrange
    data = {"_id": 17, "title": "t", "info": "i", "artist_id": 3, "file": "f"}

    # Act
    model = Painting(data)

    # Assert
    assert model.identity == 17
    assert model.title == "t"
    assert model.info == "i"
    assert model.artist_id == 3
    assert model.file == "f"


def test_painting_dto_init():
    # Arrange
    data = {"_id": 17, "title": "t", "info": "i", "artist_id": 3, "file": "f"}
    model = Painting(data)
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xaf")
        p = Path(tmp_file.name)

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        dto = PaintingDto(model)

    # Assert
    assert dto.image == "rw=="
    assert dto.id == 17
    assert dto.title == "t"
    assert dto.info == "i"
    assert dto.as_json() == {"id": 17, "image": "rw==", "title": "t", "info": "i"}

    # Cleanup
    os.remove(p)
