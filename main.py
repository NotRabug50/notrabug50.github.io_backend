from flask import Flask
from flask_session import Session
import os
import config

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Use the environment variable for MongoDB URL
app.config['MONGODB_SERVER_URL'] = os.getenv("MONGODB_SERVER_URL")

app.secret_key = os.getenv("FLASK_SECRET_KEY")

if __name__ == "__main__":
    from api import login, blog

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)
    # Start the Flask app
    app.run()
