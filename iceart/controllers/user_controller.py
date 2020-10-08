from typing import Dict

from .base_controller import BaseController


class UserController(BaseController):
    """Controller for user related requests."""

    def __init__(self, user_service):
        super().__init__("/user")
        self._user_service = user_service
        self.add_route("/", self.index, methods=["GET"])

    def index(self) -> Dict[str, str]:
        """Placeholder."""
        print(self._user_service)
        return {"msg": "Yo"}
