from .base_controller import BaseController


class ArtistController(BaseController):
    """Controller for artist related requests."""

    def __init__(self):
        super().__init__("/artist")
        self.add_route("/<int:artist_id>", self.get_artist_by_id, methods=["GET"])

    def get_artist_by_id(self, artist_id: int) -> dict:
        """Get artist by id."""
        return {}
