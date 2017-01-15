"""
Tests for our Alexa Skill
"""
import os
import json
from mock import patch
from dotenv import load_dotenv
from btvpython import alexa


SAMPLE_INTENT = """{
  "session": {
    "sessionId": "SessionId.fc225185-356d-4801-9974-39346304b4ca",
    "application": {
      "applicationId": "amzn1.ask.skill.a1422305-89ad-4b1d-a730-409ec85bcc2b"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AGIBATV336BLB4OXENW5CEINYOPN6E6QVSVLH5MOIBVIHJOGRJBJFIXNSETUTBJ3LMO5YLLZZDJD6YOO3YQKTEQJAKQOM2JLIG2EEHTYBCLKSNZQNHMFLPPQJZP3O7NA6YS7F4UG5QLEQQGSDI3AMAYOF6J3GIBS7EHXTNWT2JCYUFWK5TU6AAQDQ7YI3ANFAWOAQBJEHYKQDPY"
    },
    "new": true
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.35fdb36f-6321-466e-820a-a33a8b934de2",
    "locale": "en-US",
    "timestamp": "2017-01-15T03:35:33Z",
    "intent": {
      "name": "GetNextEvent",
      "slots": {}
    }
  },
  "version": "1.0"}"""



def setup_module(module):
    load_dotenv('.env')


def test_lambda_handler_returns_ask_json():
    response = alexa.lambda_handler(None, None)
    assert 'response' in response
    assert json.dumps(response)


def test_intent_handler():
    response = alexa.handle_intent()
    assert 'The next Burlington Python meetup is' in response


@patch('btvpython.alexa.get_next_meetup', return_value={})
def test_no_meeting_response(mock):
    response = alexa.handle_intent()
    assert 'Sorry, I could not find an upcoming event' in response


def test_meetup_client():
    assert 'MEETUP_API_KEY' in os.environ
    next_meetup = alexa.get_next_meetup('btvpython')
    assert 'title' in next_meetup
    assert 'date' in next_meetup
    assert 'venue' in next_meetup

