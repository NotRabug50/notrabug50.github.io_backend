from flask import Blueprint, request, jsonify, session
from pymongo import MongoClient
import pymongo
import hashlib
import config

login_bp = Blueprint('login', __name__)

dbclient = pymongo.MongoClient(config.MONGODB_SERVER_URL)

db = dbclient["notrabug50-main-db-02e29ccde12"]

users_collection = db["users"]

def hash_password(password):
    sha256 = hashlib.sha256()

    sha256.update(password.encode('utf-8'))

    hashed_password = sha256.hexdigest()

    return hashed_password

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    userh = users_collection.find_one({'username': username, 'password': password})

    query = {"username": username}

    doc = users_collection.find().sort("username")

    users = users_collection.find_one()["users"]
    i = 0
    print(hash_password("123q66123"))
    for x in users:
        if users[i]["username"] == username and users[i]["password"].lower() == hash_password(password):
            session['user_id'] = users[i]["id"]
            return jsonify({'message': 'Login successful'})
        i += 1
    return jsonify({'message': 'Invalid credentials'}), 401

@login_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'})
