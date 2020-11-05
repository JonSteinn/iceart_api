from typing import Dict, List

from werkzeug.exceptions import NotFound

from ..utils import get_image_as_base64_string


class ArtistViewModel:
    """Model for artists as they arrive from client."""

    # pylint: disable = duplicate-code

    def __init__(self, artist_id: int):
        if artist_id < 0:
            raise NotFound()
        self._id = artist_id

    def search_key(self) -> dict:
        """Get the model as a search key for mongo."""
        return self.__dict__

    @property
    def identity(self) -> int:
        """Getter for id."""

        return self._id


class Artist:
    """Model for artist as they are stored in the db."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, data: dict):
        self._id: int = data["_id"]
        self.title: str = data["title"]
        self.info: str = data["info"]
        self.file: str = data["file"]
        self.paintings: List[int] = data["paintings"]

    @property
    def identity(self) -> int:
        """Getter for id."""
        return self._id


class ArtistDto:
    """Model for artists as they are sent to client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, artist: Artist, thumbnails: Dict[int, str]):
        self.id = artist.identity  # pylint: disable=invalid-name
        self.title = artist.title
        self.info = artist.info
        self.image = get_image_as_base64_string(artist.file)
        self.paintings = thumbnails

    def as_json(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "info": self.info,
            "image": self.image,
            "paintings": self.paintings.copy(),
        }
