from flask import Flask
from flask_session import Session
import argparse
import os
from api import login, blog

app = Flask(__name__)

# Define command-line arguments
parser = argparse.ArgumentParser(description='Flask App with Gunicorn')
parser.add_argument('--mongodb-url', default='default_mongodb_url', help='MongoDB server URL')

# Parse command-line arguments
args = parser.parse_args()

# Configure Flask session and secret key
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'your_secret_key'
Session(app)

if __name__ == "__main__":
    # Use the MongoDB URL passed as a command-line argument
    mongodb_url = args.mongodb_url

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)

    # Start the Flask app using Gunicorn
    app.run(host='0.0.0.0', port=8000)
