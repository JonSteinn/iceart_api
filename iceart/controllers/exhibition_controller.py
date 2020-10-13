from .base_controller import BaseController


class ExhibitionController(BaseController):
    """Controller for exhibition related requests."""

    def __init__(self, exhibition_service):
        super().__init__("/exhibition")
        self.exhibition_service = exhibition_service

    def get_all_nearby_exhibitions(self):
        raise NotImplementedError
