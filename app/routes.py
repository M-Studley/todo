from flask import Blueprint, request, jsonify, make_response
from dataclasses import fields

from .database import Database
from app.models import Todo, TodoValidator

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
    try:
        # Create the Todo object
        todo_data = request.get_json()
        todo = Todo(**todo_data)

        # Validate the Todo object
        validator = TodoValidator()
        if not validator.check_all(todo):
            return make_response(jsonify({'error': 'Invalid data provided'}), 400)

        # Prepare columns and values for the SQL query
        columns = ', '.join(field.name for field in fields(Todo))
        values = tuple(getattr(todo, field.name) for field in fields(Todo) if getattr(todo, field.name) is not None)
        query = f"INSERT INTO todo ({columns}) VALUES ({', '.join(['%s'] * len(values))})"

        # Execute the query to insert the Todo
        try:
            db.execute(query, values)
            return jsonify(todo_data), 201
        except Exception as e:
            print(f'Error: {e}')
            return make_response(jsonify({'error': 'Internal Server Error'}), 500)

    except Exception as e:
        print(f'Error parsing data: {e}')
        return make_response(jsonify({'error': 'Invalid input data'}), 400)
