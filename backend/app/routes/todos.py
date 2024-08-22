import flask
from flask import request, jsonify, make_response

from . import todo_api, db
from backend.app.models.todo import Todo, TodoValidator


@todo_api.route('/todos', methods=['GET'])
def get_all_todos() -> flask.Response:
    try:
        all_data = db.fetchall('SELECT * FROM todo')
        if all_data:
            return make_response(jsonify(all_data), 200)
        else:
            db.conn.rollback()
            return make_response(jsonify({'error': 'Table empty...'}), 204)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


@todo_api.route('/todos', methods=['POST'])
def create_todo() -> flask.Response:
    try:
        # Create the to-do object
        todo_data = request.get_json()
        todo = Todo(**todo_data)

        # Validate the to-do object
        validator = TodoValidator()
        if not validator.check_all(todo):
            return make_response(jsonify({'error': 'Invalid data provided...'}), 400)

        # Prepare columns and values for the SQL query
        columns = ', '.join(key for key in todo_data.keys())
        values = tuple(value for value in todo_data.values())
        query = f"INSERT INTO todo ({columns}) VALUES ({', '.join(['%s'] * len(values))})"

        # Execute the query to insert the to-do
        try:
            db.execute(query, values)
            return make_response(jsonify(todo_data), 201)
        except Exception as e:
            db.conn.rollback()
            print(f'Error: {e}')
            return make_response(jsonify({'error': 'Internal Server Error...'}), 500)

    except Exception as e:
        print(f'Error parsing data: {e}')
        return make_response(jsonify({'error': 'Invalid input data...'}), 400)


@todo_api.route('/todos/<int:db_id>', methods=['GET'])
def get_todo_by_id(db_id) -> flask.Response:
    try:
        todo = db.fetchone('SELECT * FROM todo WHERE id = %s', (db_id,))
        if todo:
            return make_response(jsonify(todo), 200)
        else:
            return make_response(jsonify({'error': 'Todo not found...'}), 404)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


@todo_api.route('/todos/<int:db_id>', methods=['PATCH'])
def update_todo_by_id(db_id) -> flask.Response:
    try:
        # Create to-do object
        todo_data = request.get_json()
        todo = Todo(**todo_data)

        # Validate to-do object
        validate = TodoValidator()
        if not validate.check_all(todo):
            return make_response(jsonify({'error:': 'Invalid data provided...'}), 400)

        # Prepare the update query
        columns = list(key for key in todo_data.keys())
        values = list(value for value in todo_data.values())
        cols_vals = ", ".join(f"{cols} = '{vals}'" for cols, vals in zip(columns, values))
        query = f"UPDATE todo SET {cols_vals} WHERE id = %s"

        # Execute the update query
        try:
            db.execute(query, (db_id,))
            return make_response(jsonify(todo_data), 200)
        except Exception as e:
            db.conn.rollback()
            print(f'Error: {e}')
            return make_response(jsonify({'error': 'Internal Server Error...'}), 500)

    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


@todo_api.route('/todos/<int:db_id>', methods=['DELETE'])
def delete_todo(db_id):
    try:
        # Locate to-do by ID
        todo = db.fetchone('SELECT * FROM todo WHERE id = %s', (db_id,))

        if todo:
            # Execute the delete query
            db.execute('DELETE FROM todo WHERE id = %s', (db_id,))
            return make_response(jsonify({'message': 'Todo deleted successfully!'}), 200)
        else:
            return make_response(jsonify({'error': 'Todo not found...'}), 404)

    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)
