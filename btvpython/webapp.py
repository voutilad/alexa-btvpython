"""
A Flask-Ask based web app version of our Alexa skill
"""
import os
from flask import Flask, Blueprint, redirect, render_template
from flask_ask import Ask, statement, question
from btvpython.meetup import get_next_meetup

ASK_ROUTE = '/ask'
web = Blueprint('web', __name__)
ask = Ask(route=ASK_ROUTE)


@ask.launch
def welcome():
    return question(render_template('welcome'))\
        .reprompt(render_template('prompt'))


@ask.intent('GetNextEvent')
def get_next_event():
    meetup = get_next_meetup('btvpython')
    if meetup:
        return statement(render_template('next_event', **meetup))

    return statement(render_template('sorry'))


@web.route('/')
def default():
    return redirect('https://github.com/voutilad/alexa-btvpython')


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    if 'FLASK_DEBUG' in os.environ:
        app.debug = True
    app.register_blueprint(web)
    ask.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
