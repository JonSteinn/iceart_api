from typing import Iterable

from werkzeug.exceptions import BadRequest


class Exhibition:
    """Model for exhibitions as they are stored in the db."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, data: dict):
        self._id: int = data["_id"]
        self.title: str = data["title"]
        self.info: str = data["info"]
        self.latitude: float = data["latitude"]
        self.longitude: float = data["longitude"]

    @property
    def identity(self) -> int:
        """Getter for id."""
        return self._id


class ExhibitionDto:
    """Model for exhibitions as they are sent to client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, exhibition: Exhibition):
        self.id = exhibition.identity  # pylint: disable=invalid-name
        self.title = exhibition.title
        self.info = exhibition.info
        self.latitude = exhibition.latitude
        self.longitude = exhibition.longitude

    def as_json(self) -> dict:
        """Convert to dictionary."""
        return self.__dict__


class ExhibitionsDto:
    """Model for a list of exhibitions as they are sent to client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, exhibitions: Iterable[ExhibitionDto]):
        self.exhibitions = exhibitions

    def as_json(self) -> dict:
        """Convert to dictionary."""
        return {"exhibitions": [ex.as_json() for ex in self.exhibitions]}


class ExhibitionViewModel:
    """Model for exhibitions as they arrive from client."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, json_data: dict):
        lat = json_data.get("latitude", None)
        lon = json_data.get("longitude", None)
        if (
            lat is None
            or lon is None
            or not isinstance(lat, (int, float))
            or not isinstance(lon, (int, float))
        ):
            raise BadRequest()
        self.latitude = lat
        self.longitude = lon
