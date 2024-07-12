import json
from flask import Blueprint, redirect, url_for

from .database import Database

main = Blueprint('main', __name__)
db = Database()


@main.route('/', methods=['GET'])
def index():
    all_data = db.fetchall('SELECT * FROM test_todo')
    return json.dumps(all_data)


@main.route('/<title>/<description>', methods=['GET'])
def create_todo(title, description):
    db.execute(
        'INSERT INTO test_todo (title, description) VALUES (%s, %s)',
        (title, description))
    return redirect(url_for("main.index"))
