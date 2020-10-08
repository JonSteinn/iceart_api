from ..services import IPaintingService, PaintingService
from .base_controller import BaseController


class PaintingController(BaseController):
    """Controller for user related requests."""

    def __init__(self, user_service: IPaintingService = PaintingService()):
        super().__init__("/painting")
        self._user_service = user_service
        self.add_route("/<int:user_id>", self.get_by_id, methods=["GET"])

    def get_by_id(self, user_id: int) -> dict:
        """Placeholder."""
        return self._user_service.get_user_by_id(user_id)
