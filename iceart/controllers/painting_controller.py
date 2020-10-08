from ..services import IPaintingService
from .base_controller import BaseController


class PaintingController(BaseController):
    """Controller for user related requests."""

    def __init__(self, painting_service: IPaintingService):
        super().__init__("/painting")
        self._painting_service = painting_service
        self.add_route("/<int:painting_id>", self.get_painting_by_id, methods=["GET"])

    def get_painting_by_id(self, painting_id: int) -> dict:
        """Placeholder."""
        return self._painting_service.get_painting_by_id(painting_id)
