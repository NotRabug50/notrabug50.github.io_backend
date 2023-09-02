# api/blog.py

import os
import json
from flask import Blueprint, request, jsonify, session

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the absolute path to the blog.json file
json_file_path = os.path.join(current_dir, 'data/blog.json')

# Create a Blueprint for the blog API
blog_bp = Blueprint('blog', __name__)

# Load blog data from the JSON file
with open(json_file_path, 'r') as file:
    blog_data = json.load(file)

@blog_bp.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blog_data['blogs'])

@blog_bp.route('/blog/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    # Find the blog by its ID
    for blog in blog_data['blogs']:
        if blog['id'] == blog_id:
            return jsonify(blog)
    
    return jsonify({'message': 'Blog not found'})

@blog_bp.route('/post_blog', methods=['POST'])
def post_blog():
    # Check if the user is logged in using session data
    if 'user_id' not in session:
        return jsonify({'message': 'You must be logged in to post a blog'}), 401

    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    # Generate a unique ID for the new blog post
    new_blog_id = get_next_blog_id()

    # Create the new blog post
    new_blog = {'id': new_blog_id, 'title': title, 'content': content}
    blog_data['blogs'].append(new_blog)

    # Save the updated blog data to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(blog_data, file, indent=4)

    return jsonify({'message': 'Blog post created successfully', 'blog_id': new_blog_id}), 201

# Helper function to get the next available blog ID
def get_next_blog_id():
    existing_ids = {blog['id'] for blog in blog_data['blogs']}
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    return new_id

@blog_bp.route('/delete_blog/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    # Check if the user is logged in using session data
    if 'user_id' not in session:
        return jsonify({'message': 'You must be logged in to delete a blog'}), 401

    # Find the blog by its ID
    for blog in blog_data['blogs']:
        if blog['id'] == blog_id:
            # Check if the user is the author of the blog (optional)
            if blog['author_id'] != session['user_id']:
                return jsonify({'message': 'You are not authorized to delete this blog'}), 403

            # Delete the blog
            blog_data['blogs'].remove(blog)

            # Save the updated blog data to the JSON file
            with open(json_file_path, 'w') as file:
                json.dump(blog_data, file, indent=4)

            return jsonify({'message': 'Blog deleted successfully'})

    return jsonify({'message': 'Blog not found'}), 404