from os import environ
from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()

load_dotenv(_PROJECT_ROOT.joinpath(".env"))


def construct_mongo_uri_from_env() -> str:
    """Create mongodb uri from provided .env variables."""
    user = environ.get("ICEART_DB_USER")
    password = environ.get("ICEART_DB_PW")
    path = environ.get("ICEART_DB_PATH")
    if any(value is None for value in (user, password, path)):
        raise ValueError(
            (
                "Please proivde:\n\tICEART_DB_USER=\n\tICEART_DB_PW=\n\tICEART_DB_PATH="
                f"\nin {_PROJECT_ROOT.joinpath('.env').absolute().as_posix()}"
            )
        )
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
