# main.py

from flask import Flask, session
from flask_session import Session
from api import login, blog

app = Flask(__name__)

# Configure Flask-Session to use a file-based session storage
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Secret key for session management. Replace with your own secret key.
app.secret_key = 'your_secret_key'

# Register blueprints for API routes
app.register_blueprint(login.login_bp)
app.register_blueprint(blog.blog_bp)

if __name__ == "__main__":
    app.run()
