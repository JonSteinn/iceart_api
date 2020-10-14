from flask import Flask
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


def set_server_values(swag: dict):
    """Set global server values."""
    swag["info"]["version"] = "1.0"
    swag["info"]["description"] = "Server for IceArt App"
    swag["info"]["title"] = "IceArt API"
    swag["schemes"] = ["http", "https"]
    return swag


def get_ui_blueprint():
    """Get Swagger UI blueprint."""
    return get_swaggerui_blueprint(
        "/swagger",
        "http://127.0.0.1:5000/swagger/spec.json",
        config={"app_name": "Test application"},
    )


def swaggerify(app: Flask):
    """Set up swagger for app."""
    app.add_url_rule(
        "/swagger/spec.json",
        "spec",
        lambda: set_server_values(swagger(app, from_file_keyword="swag")),
    )
    app.register_blueprint(get_ui_blueprint(), url_prefix="/swagger")
