import flask
from flask import request, jsonify, make_response
from dataclasses import fields

from . import main, db
from backend.app.models.models import Todo, TodoValidator


@main.route('/todos/<int:db_id>', methods=['GET'])
def get_todo_by_id(db_id) -> flask.Response:
    try:
        todo = db.fetchone('SELECT * FROM todo WHERE id = %s', (db_id,))
        if todo:
            return jsonify(todo)
        else:
            return make_response(jsonify({'error': 'Todo not found!'}), 404)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@main.route('/todos/<int:db_id>', methods=['POST'])
def update_todo_by_id(db_id) -> flask.Response:
    try:
        # Create to-do object
        todo_data = request.get_json()
        todo = Todo(**todo_data)

        # Validate to-do object
        validate = TodoValidator()
        if not validate.check_all(todo):
            return make_response(jsonify({'error:': 'Invalid data provided!'}), 400)

        # Prepare the update query
        columns = ', '.join(f"{field.name} = %s" for field in fields(Todo))
        values = tuple(getattr(todo, field.name) for field in fields(Todo)
                       if getattr(todo, field.name) is not None) + (db_id,)
        query = f"UPDATE todo SET {columns} WHERE id = %s"

        # Execute the update query
        db.execute(query, values)
        return jsonify(todo_data)

    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({'error': 'Internal Server Error!'}), 500)
