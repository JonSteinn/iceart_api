from flask import Flask

from ..controllers import all_blueprints


def create_app() -> Flask:
    """Factory for flask app."""
    app = Flask(__name__)
    for blueprint in all_blueprints():
        app.register_blueprint(blueprint)
    return app
