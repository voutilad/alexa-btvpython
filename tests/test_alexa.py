"""
Tests for our Alexa Skill
"""
import os
import json
from mock import patch
from dotenv import load_dotenv

import meetup
from btvpython import alexa
from .fixtures import new_get_event_intent, new_launch_intent


def setup_module(module):
    load_dotenv('.env')


def test_lambda_handler_returns_data_on_get_next_event_intent():
    response = alexa.lambda_handler(new_get_event_intent(), None)
    assert 'response' in response
    assert response['response']['shouldEndSession'] is True
    assert json.dumps(response)


def test_lambda_handler_returns_a_prompt_on_launch():
    response = alexa.lambda_handler(new_launch_intent(), None)
    assert 'response' in response
    assert 'Welcome to Burlington Python' in response['response']['outputSpeech']['text']
    assert 'get next event or cancel' in response['response']['outputSpeech']['text']
    assert 'You can say' in response['response']['reprompt']['text']
    assert response['response']['shouldEndSession'] is False
    assert json.dumps(response)


def test_sorry_on_unknown_intent():
    intent = new_launch_intent()
    intent['request']['type'] = 'junk'
    response = alexa.lambda_handler(intent, None)
    assert "I'm sorry" in response['response']['outputSpeech']['text']
    assert response['response']['shouldEndSession'] is True


def test_intent_handler_for_next_event():
    response = alexa.handle_intent(alexa.NEXT_EVENT_INTENT)
    assert 'The next Burlington Python meetup is' in response


def test_intent_handler_for_cancel_event():
    response = alexa.handle_intent(alexa.CANCEL_INTENT)
    assert 'Ok, canceling.' in response


@patch('btvpython.alexa.get_next_meetup', return_value={})
def test_no_meeting_response(mock):
    response = alexa.handle_intent(alexa.NEXT_EVENT_INTENT)
    assert 'Sorry, I could not find an upcoming event' in response


def test_meetup_client():
    assert 'MEETUP_API_KEY' in os.environ
    next_meetup = meetup.get_next_meetup('btvpython')
    assert 'title' in next_meetup
    assert 'date' in next_meetup
    assert 'venue' in next_meetup


def test_convert_meetup_datetime():
    input = 1484868600000
    converted = meetup._convert_meetup_datetime(input)

    assert 'Thursday, January 19' in converted
