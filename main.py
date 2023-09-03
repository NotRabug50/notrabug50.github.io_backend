# main.py
from flask import Flask
from flask_session import Session
import argparse
import os
import config

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

if __name__ == "__main__":

    config.MONGODB_SERVER_URL = os.getenv("MONGODB_SERVER_URL")

    from api import login, blog

    app.register_blueprint(login.login_bp)
    app.register_blueprint(blog.blog_bp)
    # Start the Flask app

    from gunicorn.app.wsgiapp import WSGIApplication

    class CustomWSGIApp(WSGIApplication):
        def init(self, parser, opts, args):
            super(CustomWSGIApp, self).init(parser, opts, args)
            self.cfg.set("rabug", "rabug_backend")

    if "rabug_backend" not in os.environ:
        os.environ["rabug_backend"] = "rabug_backend"

    gunicorn_argv = ["gunicorn", "main:app"]
    CustomWSGIApp.run(gunicorn_argv)
