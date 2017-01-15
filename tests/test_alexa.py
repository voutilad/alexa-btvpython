"""
Tests for our Alexa Skill
"""
import os
from mock import patch
from dotenv import load_dotenv
from btvpython import alexa


def setup_module(module):
    load_dotenv('.env')


def test_lambda_handler():
    response = alexa.lambda_handler(None, None)
    assert 'The next Burlington Python meetup is' in response


@patch('btvpython.alexa.get_next_meetup', return_value={})
def test_no_meeting_response(mock):
    response = alexa.lambda_handler(None, None)
    assert 'Sorry, I could not find an upcoming event' in response


def test_meetup_client():
    assert 'MEETUP_API_KEY' in os.environ
    next_meetup = alexa.get_next_meetup('btvpython')
    assert 'title' in next_meetup
    assert 'date' in next_meetup
    assert 'venue' in next_meetup
