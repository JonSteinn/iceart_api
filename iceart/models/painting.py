from werkzeug.exceptions import NotFound

from ..utils import get_image_as_base64_string


class PaintingViewModel:
    """Model for paintings as they arrive from client."""

    # pylint: disable = duplicate-code

    def __init__(self, painting_id: int):
        if painting_id < 0:
            raise NotFound()
        self._id = painting_id

    def search_key(self) -> dict:
        """Get the model as a search key for mongo."""
        return self.__dict__

    @property
    def identity(self) -> int:
        """Getter for id."""
        return self._id


class Painting:
    """Model for paintings as they are stored in the db."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, data: dict):
        self._id: int = data["_id"]
        self.title: str = data["title"]
        self.artist_id: int = data["artist_id"]
        self.file: str = data["file"]
        self.technique: str = data["technique"]
        self.year: int = data["year"]

    @property
    def identity(self) -> int:
        """Getter for id."""
        return self._id


class PaintingDto:
    """Model for paintings as they are sent to client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, painting: Painting):
        self.id = painting.identity  # pylint: disable=invalid-name
        self.title = painting.title
        self.technique = painting.technique
        self.year = painting.year
        self.image = get_image_as_base64_string(painting.file)
        self.artist = painting.artist_id

    def as_json(self) -> dict:
        """Convert to dictionary."""
        return self.__dict__
