from flask import Flask
from backend.app.routes.todos import main
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register main blueprint
    app.register_blueprint(main)

    return app
