from flask import Blueprint
from backend.app.database.database import Database

api = Blueprint('api', __name__)
db = Database()
