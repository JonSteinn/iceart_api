from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.exceptions import HTTPException

from ..controllers import PaintingController
from ..repositories import PaintingRepository
from ..services import PaintingService
from .config import Config


def get_injected_painting_controller(mongo: PyMongo) -> PaintingController:
    """Placeholder, do this better..."""
    return PaintingController(PaintingService(PaintingRepository(mongo.db)))


def create_app(mongo: PyMongo, cfg: Config) -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)

    app.register_error_handler(
        Exception, lambda e: ({}, e.code if isinstance(e, HTTPException) else 500)
    )

    app.config.from_object(cfg)

    mongo.init_app(app)

    app.register_blueprint(get_injected_painting_controller(mongo))

    return app
