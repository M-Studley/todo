from flask import Blueprint
from backend.app.database.database import Database

todo_api = Blueprint('todo_api', __name__)
user_api = Blueprint('user_api', __name__)
db = Database()
