from flask import Flask
from backend.app.routes.todos import api
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register main blueprint
    app.register_blueprint(api)

    return app
