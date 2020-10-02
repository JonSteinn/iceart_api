from typing import Dict

from flask import Blueprint

demo = Blueprint("demo", __name__, url_prefix="/demo")


@demo.route("/", methods=["GET"])
def index() -> Dict:
    """Hello world example."""
    return {"message": "Hello world!"}


@demo.route("/<name>", methods=["GET"])
def greet(name: str) -> Dict:
    """Personalised hello example."""
    return {"message": f"Hello {name}"}
