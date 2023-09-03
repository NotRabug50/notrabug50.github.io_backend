from flask import Blueprint, request, jsonify, session
from pymongo import MongoClient
import pymongo
import config

blog_bp = Blueprint('blog', __name__)

dbclient = pymongo.MongoClient(config.MONGODB_SERVER_URL)

db = dbclient["notrabug50-main-db-02e29ccde12"]

blog_collection = db["blogs"]

@blog_bp.route('/delete_blog/<blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    if 'user_id' not in session:
        return jsonify({'message': 'You must be logged in to delete a blog'}), 401

    from bson import ObjectId
    blog_id = ObjectId(blog_id)

    blog = blog_collection.find_one({'_id': blog_id})

    if not blog:
        return jsonify({'message': 'Blog post not found'}), 404

    if blog['author_id'] != session['user_id']:
        return jsonify({'message': 'You can only delete your own blog posts'}), 403

    blog_collection.delete_one({'_id': blog_id})

    return jsonify({'message': 'Blog post deleted successfully'}), 200

@blog_bp.route('/get_blogs', methods=['GET'])
def get_blogs():
    blogs = list(blog_collection.find())

    for blog in blogs:
        blog['_id'] = str(blog['_id'])

    return jsonify({'blogs': blogs}), 200
