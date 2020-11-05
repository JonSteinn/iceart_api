import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest
import pytest_mock
from werkzeug.exceptions import NotFound

from iceart.models import Artist, ArtistDto, ArtistViewModel


def test_artist_vm_init():
    with pytest.raises(NotFound):
        ArtistViewModel(-1)


def test_artist_vm_search_key():
    assert ArtistViewModel(44).search_key() == {"_id": 44}


def test_artist_init():
    # Arrange
    data = {"_id": 44, "title": "t", "info": "i", "file": "f", "paintings": [5, 3, 77]}

    # Act
    model = Artist(data)

    # Assert
    assert model.identity == 44
    assert model.title == "t"
    assert model.info == "i"
    assert model.file == "f"
    assert model.paintings == [5, 3, 77]


def test_artist_dto_init():
    # Arrange
    data = {"_id": 44, "title": "t", "info": "i", "file": "f", "paintings": [5, 3, 77]}
    model = Artist(data)
    with NamedTemporaryFile("w+b", delete=False) as tmp_file:
        tmp_file.write(b"\xab\xef")
        p = Path(tmp_file.name)

    # Act
    with pytest_mock.mock.patch("pathlib.Path.joinpath", return_value=p):
        dto = ArtistDto(model, {1: "img1", 2: "img2"})

    # Assert
    assert dto.image == "q+8="
    assert dto.id == 44
    assert dto.title == "t"
    assert dto.info == "i"
    assert dto.as_json() == {
        "id": 44,
        "title": "t",
        "info": "i",
        "image": "q+8=",
        "paintings": {1: "img1", 2: "img2"},
    }
    assert dto.paintings == {1: "img1", 2: "img2"}

    # Cleanup
    os.remove(p)
