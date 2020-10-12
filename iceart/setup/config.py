from os import environ

from dotenv import load_dotenv

from ..utils import get_abs_path

_DEFAULT_VALUE = "?"

load_dotenv(get_abs_path(".env"))


def construct_mongo_uri_from_env() -> str:
    """Create mongodb uri from provided .env variables."""
    user = environ.get("ICEART_DB_USER", _DEFAULT_VALUE)
    password = environ.get("ICEART_DB_PW", _DEFAULT_VALUE)
    path = environ.get("ICEART_DB_PATH", _DEFAULT_VALUE)
    return f"mongodb+srv://{user}:{password}@{path}?retryWrites=true&w=majority"


class Config:
    """Base config."""

    # pylint: disable=too-few-public-methods

    STATIC_FOLDER = "static"
    MONGO_URI = construct_mongo_uri_from_env()


class ProdConfig(Config):
    """Production configuration."""

    # pylint: disable=too-few-public-methods

    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """Development configuration."""

    # pylint: disable=too-few-public-methods

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""

    # pylint: disable=too-few-public-methods

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
