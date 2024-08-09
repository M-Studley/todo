from flask import Blueprint
from backend.app.database.database import Database

main = Blueprint('main', __name__)
db = Database()
