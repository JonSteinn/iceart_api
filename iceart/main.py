from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Temp hello world!"""
    return {"message": "I'm a json object!"}


def main() -> None:
    """Starting point."""
    app.run()


if __name__ == "__main__":
    main()
