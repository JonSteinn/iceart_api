from flask import Flask

from ..controllers import UserController


def create_app() -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)
    app.register_blueprint(UserController(None))
    return app
