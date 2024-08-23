import flask
from flask import request, jsonify, make_response

from . import user_api, db
from backend.app.models.user import User, UserValidator
from backend.app.utils.password_manager import PasswordManager


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
    try:
        # Create User object
        user_data = request.get_json()
        user = User(**user_data)

        # validate the User
        validator = UserValidator()
        if not validator.check_all(user):
            return make_response(jsonify({'error': 'Invalid data provided...'}), 400)

        # hash password
        ph = PasswordManager()
        hashed_pw = ph.hasher(user.password)

        if hashed_pw:
            user.password = hashed_pw

        # Prepare columns and values for the SQL query
        columns = ', '.join(key for key in user.__dict__.keys())
        values = tuple(value for value in user.__dict__.values())
        query = f"INSERT INTO user ({columns}) VALUES ({', '.join(['%s'] * len(values))})"

        # Execute the query to insert the to-do
        try:
            db.execute(query, values)
            return make_response(jsonify(user.__dict__), 201)

        except Exception as e:
            db.conn.rollback()
            print(f'error: {e}')
            return make_response(jsonify({'error': 'Internal Server Error...'}), 500)

    except Exception as e:
        print(f'Error parsing data: {e}')
        return make_response(jsonify({'error': 'Invalid input data...'}), 400)


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
    try:
        # Create user object
        user_data = request.get_json()
        user = User(**user_data)

        # Validate user object
        validate = UserValidator()
        if not validate.check_all(user):
            return make_response(jsonify({'error:': 'Invalid data provided...'}), 400)

        # Prepare the update query
        columns = list(key for key in user.__dict__.keys())
        values = list(value for value in user.__dict__.values())
        cols_vals = ", ".join(f"{cols} = '{vals}'" for cols, vals in zip(columns, values))
        query = f"UPDATE user SET {cols_vals} WHERE id = %s"

        # Execute the update query
        try:
            db.execute(query, (db_id,))
            return make_response(jsonify(user.__dict__), 200)
        except Exception as e:
            db.conn.rollback()
            print(f'error: {e}')
            return make_response(jsonify({'error': 'Internal Server Error...'}), 500)

    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({'error': 'Internal Server Error...'}), 500)


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
