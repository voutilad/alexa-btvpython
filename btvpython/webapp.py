"""
A Flask-Ask based web app version of our Alexa skill
"""
import os
from flask import Flask
from flask_ask import Ask

ASK_ROUTE = '/ask'

ask = Ask(route=ASK_ROUTE)


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    if 'FLASK_DEBUG' in os.environ:
        app.debug = True
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
