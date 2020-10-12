from itertools import chain

import pytest
from werkzeug.exceptions import BadRequest

from iceart.models import ImageViewModel


def test_image_vm_missing_key():
    with pytest.raises(BadRequest):
        ImageViewModel({})


def test_image_vm_not_str():
    with pytest.raises(BadRequest):
        ImageViewModel({"img": False})


def test_image_vm_non_ascii():
    with pytest.raises(BadRequest):
        ImageViewModel({"img": "Þ"})


def test_image_vm_non_64base():
    with pytest.raises(BadRequest):
        ImageViewModel({"img": "."})


def test_image_vm_valid():
    ImageViewModel(
        {
            "img": "".join(
                chain(
                    (chr(ord("a") + i) for i in range(26)),
                    (chr(ord("A") + i) for i in range(26)),
                    (chr(ord("0") + i) for i in range(10)),
                    ("+", "/"),
                )
            )
        }
    )
