import json
from flask import Blueprint, request, jsonify, redirect, url_for

from .database import Database

main = Blueprint('main', __name__)
db = Database()


@main.route('/todos', methods=['GET'])
def get_all_todos():
    try:
        all_data = db.fetchall('SELECT * FROM todo')
        if all_data:
            return json.dumps(all_data)
    except Exception as e:
        print(f'Error: {e}')


@main.route('/todos', methods=['POST'])
def create_todo():
    # Extracting json data
    data = request.get_json()
    if not data:
        print('No data extracted...')
    # Extracting keys and values
    columns = ', '.join(data.keys())
    values = tuple(data.values())
    # Constructing query
    query = f"INSERT INTO todo ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
    # Executing query
    try:
        db.execute(query, values)
        return jsonify(data), 201
    except Exception as e:
        print(f'Error: {e}')

    return redirect(url_for('get_all_todos'))
