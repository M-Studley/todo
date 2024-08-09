from flask import Flask
from app.routes import main
from app.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register main blueprint
    app.register_blueprint(main)

    return app
