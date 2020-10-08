from .db import mongo
from .setup import create_app


def main() -> None:
    """Starting point."""
    app = create_app(mongo)
    app.run()


if __name__ == "__main__":
    main()
