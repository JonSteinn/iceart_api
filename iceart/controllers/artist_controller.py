from ..services import IArtistService
from .base_controller import BaseController


class ArtistController(BaseController):
    """Controller for artist related requests."""

    def __init__(self, artist_service: IArtistService):
        super().__init__("/artist")
        self._artist_service = artist_service
        self.add_route("/<int:artist_id>", self.get_artist_by_id, methods=["GET"])

    def get_artist_by_id(self, artist_id: int) -> dict:
        """Get artist by id.

        swag: iceart/resources/swagger/artist_controller/get_artist_by_id.yml
        """
        return self._artist_service.get_artist_by_id(artist_id).as_json()
