# main.py
from flask import Flask
from flask_session import Session
import argparse
import os
import config

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.secret_key = 'your_secret_key'

if __name__ == "__main__":

    config.MONGODB_SERVER_URL = os.getenv("MONGODB_SERVER_URL")

    from api import login, blog

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)
    # Start the Flask app
    app.run()
