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
def update_todo_by_id(db_id):
    # Create to-do object
    todo_data = request.get_json()
    todo = Todo(**todo_data)
    ...
