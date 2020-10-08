from flask import Flask

from ..controllers import PaintingController


def create_app() -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)
    app.register_blueprint(PaintingController())
    return app
