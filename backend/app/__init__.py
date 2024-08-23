from flask import Flask

from backend.app.routes import todo_api, user_api
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(blueprint=todo_api, url_prefix='/todos')
    app.register_blueprint(blueprint=user_api, url_prefix='/users')

    # Initialize the Database
    Database.init()

    print(app.url_map)

    return app
