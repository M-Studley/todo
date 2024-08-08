from flask import Blueprint, request, jsonify, make_response

from .database import Database

main = Blueprint('main', __name__)
db = Database()


@main.route('/todos', methods=['GET'])
def get_all_todos():
    try:
        all_data = db.fetchall('SELECT * FROM todo')
        if all_data:
            return jsonify(all_data)
        else:
            return make_response(jsonify([]), 204)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@main.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data:
        return make_response(jsonify({'error': 'No data provided'}), 400)

    columns = ', '.join(data.keys())
    values = tuple(data.values())
    query = f"INSERT INTO todo ({columns}) VALUES ({', '.join(['%s'] * len(values))})"

    try:
        db.execute(query, values)
        return jsonify(data), 201
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)
