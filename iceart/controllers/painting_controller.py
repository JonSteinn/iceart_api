from flask import request

from ..services import IPaintingService
from .base_controller import BaseController


class PaintingController(BaseController):
    """Controller for user related requests."""

    def __init__(self, painting_service: IPaintingService):
        super().__init__("/painting")
        self._painting_service: IPaintingService = painting_service
        self.add_route("/<int:painting_id>", self.get_painting_by_id, methods=["GET"])
        self.add_route("", self.upload_painting, methods=["POST"])

    def get_painting_by_id(self, painting_id: int) -> dict:
        """Placeholder.

        swag: iceart/resources/swagger/painting_controller/get_painting_by_id.yml
        """
        return self._painting_service.get_painting_by_id(painting_id).as_json()

    def upload_painting(self) -> dict:
        """Upload a jpeg image.

        swag: iceart/resources/swagger/painting_controller/upload_painting.yml
        """
        data = request.get_json()
        return self._painting_service.get_akin_painting(data).as_json()
