import base64
from typing import List, Tuple

import cv2
import imagehash
import numpy as np
from PIL import Image

from .path_manager import get_image_path

_HASH_SIZE = 128
_THUMBNAIL_DIM = (100, 100)
_CROP_LIMIT = 500
_THRESH_LEVEL = 150

Rect = Tuple[int, int, int, int]


def get_image_as_thumbnail(img_path: str) -> str:
    """Scale image to thumbnail size."""
    src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(src, _THUMBNAIL_DIM)
    jpg = cv2.imencode(".jpg", resized)[1].tostring()
    b64 = base64.b64encode(jpg)
    return b64.decode("ascii")


def create_image_hash_from_bytes(b_img: bytes) -> np.ndarray:
    """Create a numpy 01 hash array for image bytes."""
    im_arr = np.frombuffer(b_img, dtype=np.uint8)
    image = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    hash_image = _create_image_hash(Image.fromarray(_crop_image(image)))
    return hash_image


def create_image_hash_from_file(filename: str) -> np.ndarray:
    """Create a numpy 01 hash array for the given image file."""
    return _create_image_hash(Image.open(get_image_path(filename).as_posix()))


def get_image_hash_difference(hash1: np.ndarray, hash2: np.ndarray) -> int:
    """Count different fields in binary hash arrays."""
    difference: int = np.count_nonzero(hash1 != hash2)
    return difference


def get_most_difference() -> int:
    """The maximum number of difference in a hash compare array."""
    return _HASH_SIZE ** 2 + 1


def _create_image_hash(img: np.ndarray) -> np.ndarray:
    return imagehash.phash(img, _HASH_SIZE).hash + imagehash.whash(img, _HASH_SIZE).hash


def _crop_image(img: np.ndarray) -> np.ndarray:
    contours = _get_contours(img)
    bounds = _get_boundaries(img, contours)
    cropped = _crop(img, bounds)
    if _get_size(cropped) < _CROP_LIMIT:
        return img
    return cropped


def _get_contours(img: np.ndarray) -> List[np.ndarray]:
    """Threshold the image and get contours."""
    # First make the image 1-bit and get contours
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the right threshold level
    tresh_level: int = _THRESH_LEVEL
    _, thresh = cv2.threshold(imgray, tresh_level, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)
    # filter contours that are too large or small
    return [contour for contour in contours if _contour_ok(img, contour)]


def _get_size(img: np.ndarray) -> int:
    """Return the size of the image in pixels."""
    height, width = img.shape[:2]
    square: int = height * width
    return square


def _contour_ok(img: np.ndarray, contour: np.ndarray) -> bool:
    """Check if the contour is a good predictor of photo location."""
    _, _, width, height = cv2.boundingRect(contour)
    if width < 50 or height < 50:
        return False  # too narrow or wide is bad
    area = cv2.contourArea(contour)
    if area > _get_size(img) * 0.5:
        return False
    if area < 200:
        return False
    return True


def _get_boundaries(img: np.ndarray, contours: np.ndarray) -> Rect:
    """Find the boundaries of the photo in the image using contours."""
    # margin is the minimum distance from the edges of the image, as a fraction
    height, width = img.shape[:2]
    minx, miny, maxx, maxy = width, height, 0, 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(maxx, x + w)
        maxy = max(maxy, y + h)
    return minx, miny, maxx, maxy


def _crop(img: np.ndarray, boundaries: Rect) -> np.ndarray:
    """Crop the image to the given boundaries."""
    minx, miny, maxx, maxy = boundaries
    return img[miny:maxy, minx:maxx]
