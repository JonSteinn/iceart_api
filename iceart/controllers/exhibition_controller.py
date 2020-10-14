from flask import request

from ..services import IExhibitionService
from .base_controller import BaseController


class ExhibitionController(BaseController):
    """Controller for exhibition related requests."""

    def __init__(self, exhibition_service: IExhibitionService):
        super().__init__("/exhibition")
        self._exhibition_service = exhibition_service
        self.add_route("", self.get_all_nearby_exhibitions, methods=["POST"])

    def get_all_nearby_exhibitions(self):
        """Get all nearby exhibitions.

        swag: iceart/resources/swagger/\
exhibition_controller/get_all_nearby_exhibitions.yml
        """
        data = request.get_json()
        return self._exhibition_service.get_all_nearby_exhibitions(data).as_json()
