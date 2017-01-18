"""
A Flask-Ask based web app version of our Alexa skill
"""
import os
from flask import Flask
from flask_ask import Ask, statement, question
from btvpython.meetup import get_next_meetup

ASK_ROUTE = '/ask'

ask = Ask(route=ASK_ROUTE)


@ask.launch
def welcome():
    msg = 'Welcome to Burlington Python'
    prompt = 'You can say get next event or cancel.'
    return question(msg + ', ' + prompt).reprompt(prompt)


@ask.intent('GetNextEvent')
def get_next_event():
    meetup = get_next_meetup('btvpython')
    if meetup:
        msg = 'The next Burlington Python meetup is "{title}" on {date} at {venue}'
        return statement(msg.format(**meetup))

    return statement('Sorry, I could not find an upcoming event for Burlington Python.')


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    if 'FLASK_DEBUG' in os.environ:
        app.debug = True
    ask.init_app(app)
    return app


def wsgi():
    app = create_app()
    app.run()


if __name__ == '__main__':
    wsgi()
