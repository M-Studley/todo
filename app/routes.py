import json
from flask import Blueprint, request, jsonify

from .database import Database

main = Blueprint('main', __name__)
db = Database()


@main.route('/todos', methods=['GET'])
def get_all_todos():
    all_data = db.fetchall('SELECT * FROM test_todo')
    return json.dumps(all_data)


@main.route('/todos', methods=['POST'])
def create_todo():
    # Extracting json data
    data = request.get_json()
    # Extracting keys and values
    columns = ', '.join(data.keys())
    values = tuple(data.values())
    # Constructing query
    query = f"INSERT INTO test_todo ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
    # Executing query
    db.execute(query, values)
    return jsonify(data), 201
