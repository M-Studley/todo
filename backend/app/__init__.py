from flask import Flask

from backend.app.routes.todos import todo_api
# from backend.app.routes.users import user_api
from backend.app.database.database import Database


def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(todo_api, url_prefix='/todos')
    # app.register_blueprint(user_api, url_prefix='/users')

    # Initialize Database
    Database.init()

    print("Blueprints registered:")
    print(app.url_map)

    return app
