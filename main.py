# main.py
from flask import Flask
from flask_session import Session
import sys
import argparse
import config  # Import your configuration settings

app = Flask(__name__)

# Configure Flask-Session to use a file-based session storage
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Set the secret key from your configuration
app.secret_key = 'your_secret_key'

# Register blueprints for API routes


if __name__ == "__main__":

    # Use the provided MongoDB server URL
    config.MONGODB_SERVER_URL = sys.argv[1]

    from api import login, blog

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)
    # Start the Flask app
    app.run(debug=True)
