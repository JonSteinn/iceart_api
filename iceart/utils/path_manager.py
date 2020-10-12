from pathlib import Path

_PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()


def get_abs_path(*args) -> Path:
    """Get absolute path to a path relative to project root."""
    return _PROJECT_ROOT.joinpath(*args)


def get_image_path(file_name) -> Path:
    """Get absolute path to an image path."""
    return get_abs_path("iceart", "resources", "images", file_name)
