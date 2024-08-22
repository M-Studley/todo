import flask
from flask import request, jsonify, make_response

from . import user_api, db
from backend.app.models.user import User, UserValidator


@user_api.route('/users', methods=['GET'])
def get_all_users() -> flask.Response:
    try:
        all_data = db.fetchall('SELECT * FROM user')
        if all_data:
            return make_response(jsonify(all_data), 200)
        else:
            db.conn.rollback()
            return make_response(jsonify({'error': 'Table empty...'}), 204)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


@user_api.route('/users', methods=['POST'])
def create_user() -> flask.Response:
    ...


@user_api.route('/users/<int:db_id>', methods=['GET'])
def get_user_by_id(db_id) -> flask.Response:
    try:
        user = db.fetchone('SELECT * FROM user WHERE id = %s', (db_id,))
        if user:
            return make_response(jsonify(user), 200)
        else:
            return make_response(jsonify({'error': 'User not found...'}), 404)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


@user_api.route('/users/<int:db_id>', methods=['PATCH'])
def update_user_by_id(db_id) -> flask.Response:
    ...


@user_api.route('/users/<int:db_id>', methods=['DELETE'])
def delete_user(db_id):
    try:
        # Locate to-do by ID
        user = db.fetchone('SELECT * FROM user WHERE id = %s', (db_id,))

        if user:
            # Execute the delete query
            db.execute('DELETE FROM user WHERE id = %s', (db_id,))
            return make_response(jsonify({'message': 'User deleted successfully!'}), 200)
        else:
            return make_response(jsonify({'error': 'User not found...'}), 404)

    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)
