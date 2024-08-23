from flask import Flask

import backend.app.routes
from backend.app.routes.__init__ import todo_api, user_api
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(todo_api)
    app.register_blueprint(user_api)

    print(app.url_map)

    return app
