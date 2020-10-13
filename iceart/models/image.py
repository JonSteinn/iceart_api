import binascii
from base64 import b64decode

from werkzeug.exceptions import BadRequest


class ImageViewModel:
    """Model for images as they arrive from client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, json_data: dict):
        img_str = json_data.get("image", None)
        if img_str is None or not isinstance(img_str, str):
            raise BadRequest()
        try:
            self.image: bytes = b64decode(img_str, validate=True)
        except (binascii.Error, ValueError) as error:
            raise BadRequest() from error
