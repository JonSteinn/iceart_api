import sys

from .db import mongo
from .setup import DevConfig, create_app, swaggerify


def main() -> None:
    """Starting point."""
    cfg = DevConfig()
    app = create_app(mongo, cfg)
    swaggerify(app)
    if len(sys.argv) > 1:
        app.run(host=sys.argv[1])
    else:
        app.run()


if __name__ == "__main__":
    main()
