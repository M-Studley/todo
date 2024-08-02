from flask import Flask
from .routes import main
from .database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register main blueprint
    app.register_blueprint(main)

    return app
