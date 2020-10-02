from .setup import create_app


def main() -> None:
    """Starting point."""
    app = create_app()
    app.run()


if __name__ == "__main__":
    main()
