import cv2
import imagehash
import numpy as np

_HASH_SIZE = 128
_MOST_DIFF = _HASH_SIZE ** 2


def create_image_hash(img: np.ndarray) -> np.ndarray:
    """Create a numpy 01 hash array for image."""
    return imagehash.phash(img, _HASH_SIZE).hash + imagehash.whash(img, _HASH_SIZE).hash


def get_most_difference() -> int:
    """The maximum number of difference in a hash compare array."""
    return _HASH_DIFF


def crop_image(img: bytes) -> np.ndarray:
    """Crop a loaded image"""
    contours = _get_contours(img)
    bounds = _get_boundaries(img, contours)
    cropped = _crop(img, bounds)
    if _get_size(cropped) < 100000:
        return img
    return cropped


def _get_contours(img):
    """Threshold the image and get contours."""
    # First make the image 1-bit and get contours
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the right threshold level
    tl: int = 100
    _, thresh = cv2.threshold(imgray, tl, 255, 0)
    while _white_percent(thresh) > 0.85:
        tl += 10
        _, thresh = cv2.threshold(imgray, tl, 255, 0)

    contours, _ = cv2.findContours(thresh, 1, 2)

    # filter contours that are too large or small
    contours = [cc for cc in contours if _contour_ok(img, cc)]
    return contours


def _get_size(img):
    """Return the size of the image in pixels."""
    ih, iw = img.shape[:2]
    return iw * ih


def _white_percent(img):
    """Return the percentage of the thresholded image that's white."""
    return cv2.countNonZero(img) / _get_size(img)


def _contour_ok(img, cc):
    """Check if the contour is a good predictor of photo location."""
    if _near_edge(img, cc):
        return False  # shouldn't be near edges
    _, _, w, h = cv2.boundingRect(cc)
    if w < 100 or h < 100:
        return False  # too narrow or wide is bad
    area = cv2.contourArea(cc)
    if area > _get_size(img) * 0.3:
        return False
    if area < 200:
        return False
    return True


def _near_edge(img, contour):
    """Check if a contour is near the edge in the given image."""
    x, y, w, h = cv2.boundingRect(contour)
    ih, iw = img.shape[:2]
    mm = 80  # margin in pixels
    return x < mm or x + w > iw - mm or y < mm or y + h > ih - mm


def _get_boundaries(img, contours):
    """Find the boundaries of the photo in the image using contours."""
    # margin is the minimum distance from the edges of the image, as a fraction
    ih, iw = img.shape[:2]
    minx = iw
    miny = ih
    maxx = 0
    maxy = 0

    for cc in contours:
        x, y, w, h = cv2.boundingRect(cc)
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x + w > maxx:
            maxx = x + w
        if y + h > maxy:
            maxy = y + h

    return (minx, miny, maxx, maxy)


def _crop(img, boundaries):
    """Crop the image to the given boundaries."""
    minx, miny, maxx, maxy = boundaries
    return img[miny:maxy, minx:maxx]
