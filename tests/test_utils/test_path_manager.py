from pathlib import Path

from iceart.utils import get_abs_path, get_image_path


def test_get_abs_path():
    # Arrange
    root = Path(__file__).parent.parent.parent.absolute()

    # Act
    path1 = get_abs_path("x.txt")
    path2 = get_abs_path("dir1", "dir2", "file.exe")

    # Assert
    assert path1.relative_to(root).as_posix() == "x.txt"
    assert path2.relative_to(root).as_posix() == "dir1/dir2/file.exe"


def test_get_image_path():
    # Arrange
    root = Path(__file__).parent.parent.parent.absolute()

    # Act
    path = get_image_path("boot.png")

    # Assert
    assert path.relative_to(root).as_posix() == "iceart/resources/images/boot.png"
