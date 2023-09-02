# api/login.py

import os
import json
from flask import Blueprint, request, jsonify, session

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the absolute path to the users.json file
json_file_path = os.path.join(current_dir, 'users.json')

# Create a Blueprint for the login API
login_bp = Blueprint('login', __name__)

# Load user data from the JSON file
with open(json_file_path, 'r') as file:
    users_data = json.load(file)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the provided username and password match any user in the JSON data
    for user in users_data['users']:
        if user['username'] == username and user['password'] == password:
            # Generate a session token and store user information in the session
            session['user_id'] = user['id']
            session['username'] = user['username']
            return jsonify({'message': 'Login successful', 'user_id': user['id'], 'username': user['username']})

    return jsonify({'message': 'Login failed'})

@login_bp.route('/logout', methods=['POST'])
def logout():
    # Clear the session data to log out the user
    session.clear()
    return jsonify({'message': 'Logged out successfully'})
