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
app.secret_key = app.config["FLASK_SECRET_KEY"]
Session(app)

# ...

if __name__ == "__main__":
    mongodb_url = app.config['MONGODB_SERVER_URL']

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)

    # Start the Flask app using Gunicorn
    app.run()

