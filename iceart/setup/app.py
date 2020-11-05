from typing import Iterator

from flask import Flask
from flask_caching import Cache
from flask_pymongo import PyMongo

from ..controllers import (
    ArtistController,
    BaseController,
    ExhibitionController,
    PaintingController,
)
from ..repositories import ArtistRepository, ExhibitionRepository, PaintingRepository
from ..services import (
    ArtistService,
    ExhibitionService,
    MachineLearningService,
    PaintingService,
)
from .config import Config
from .error_handler import ErrorHandler


def get_injected_controllers(mongo: PyMongo, cache: Cache) -> Iterator[BaseController]:
    """Placeholder, do this better..."""
    p_repo = PaintingRepository(mongo.db, cache)
    e_repo = ExhibitionRepository(mongo.db, cache)
    a_repo = ArtistRepository(mongo.db, cache)
    yield PaintingController(
        PaintingService(p_repo, MachineLearningService(p_repo, cache))
    )
    yield ExhibitionController(ExhibitionService(e_repo))
    yield ArtistController(ArtistService(a_repo))


def create_app(mongo: PyMongo, cfg: Config) -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)

    app.config.from_object(cfg)

    error_handler = ErrorHandler(app.config["DEBUG"])
    app.register_error_handler(Exception, error_handler.get_handler())

    mongo.init_app(app)

    cache = Cache(app)

    for blueprint in get_injected_controllers(mongo, cache):
        app.register_blueprint(blueprint)

    return app
