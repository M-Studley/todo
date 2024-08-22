from flask import Flask
from backend.app.routes import todo_api, user_api
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register todo_api blueprint
    app.register_blueprint(todo_api)

    # Register user_api blueprint
    app.register_blueprint(user_api)

    return app
