from typing import Iterable

from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.exceptions import HTTPException

from ..controllers import BaseController, PaintingController
from ..repositories import PaintingRepository
from ..services import MachineLearningService, PaintingService
from .config import Config


def get_injected_controllers(mongo: PyMongo) -> Iterable[BaseController]:
    """Placeholder, do this better..."""
    p_repo = PaintingRepository(mongo.db)
    yield PaintingController(PaintingService(p_repo, MachineLearningService(p_repo)))


def create_app(mongo: PyMongo, cfg: Config) -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)

    app.register_error_handler(
        Exception, lambda e: ({}, e.code if isinstance(e, HTTPException) else 500)
    )

    app.config.from_object(cfg)

    mongo.init_app(app)

    for blueprint in get_injected_controllers(mongo):
        app.register_blueprint(blueprint)

    return app
