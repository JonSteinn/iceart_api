from flask import Flask
from flask_pymongo import PyMongo

from ..controllers import PaintingController
from ..repositories import PaintingRepository
from ..services import PaintingService


def get_injected_painting_controller(mongo: PyMongo) -> PaintingController:
    """Placeholder, do this better..."""
    return PaintingController(PaintingService(PaintingRepository(mongo.db)))


def create_app(mongo: PyMongo) -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo.init_app(app)

    app.register_blueprint(get_injected_painting_controller(mongo))

    return app
