from base64 import b64encode

from .path_manager import get_image_path


def get_image_as_bytes(file_name) -> bytes:
    """Get image as bytes."""
    with get_image_path(file_name).open("r+b") as f:
        return f.read()


def get_image_as_base64_string(file_name) -> str:
    """Get image as base64 string."""
    return b64encode(get_image_as_bytes(file_name)).decode("ascii")
