from flask import Flask

from ..controllers import PaintingController
from ..repositories import PaintingRepository
from ..services import PaintingService


def get_injected_painting_controller() -> PaintingController:
    """Placeholder, do this better..."""
    return PaintingController(PaintingService(PaintingRepository()))


def create_app() -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)
    app.register_blueprint(get_injected_painting_controller())
    return app
