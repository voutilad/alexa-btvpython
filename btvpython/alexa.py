"""
Our Alexa Skill for BTVPython
"""
import os

from .meetup import get_next_meetup

NEXT_EVENT_INTENT = 'GetNextEvent'
CANCEL_INTENT = 'AMAZON.CancelIntent'


def _new_response():
    return {
        'version': 1.0,
        'sessionAttributes': {},
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': ''
            },
            'card': {
                'type': 'Simple',
                'title': 'BTV Python',
                'content': ''
            },
            'shouldEndSession': True
        }
    }


def handle_intent(intent):
    """
    Right now we'll just handle all intents as a request for the next meeting
    :return: message String
    """
    if intent == NEXT_EVENT_INTENT:
        msg = 'The next Burlington Python meetup is "{title}" on {date} at {venue}'
        meetup = get_next_meetup('btvpython')
        if meetup:
            return msg.format(**meetup)
        else:
            return 'Sorry, I could not find an upcoming event for Burlington Python.'
    elif intent == CANCEL_INTENT:
        return 'Ok, canceling.'
    else:
        return "I'm sorry, I couldn't handle your request."


def lambda_handler(event, context):
    """
    Our main entry point for AWS Lambda via Alexa
    :param event: Alexa Request
    :param context: Lambda context
    :return: Alexa Response
    """
    if 'DEBUG_LAMBDA' in os.environ:
        print('event: ' + str(event))
        print('context: ' + str(context))

    response = _new_response()
    if event['request']['type'] == 'LaunchRequest':
        message = 'Welcome to Burlington Python, you can say get next event or cancel!'
        response['response']['shouldEndSession'] = False
        response['response']['reprompt'] = {
            'type': 'PlainText',
            'text': 'You can say get next event or cancel.'
        }
    elif event['request']['type'] == 'IntentRequest':
        message = handle_intent(event['request']['intent']['name'])
    else:
        message = "I'm sorry, but I don't know how to handle your request."

    response['response']['outputSpeech']['text'] = message
    response['response']['card']['content'] = message

    if 'DEBUG_LAMBDA' in os.environ:
        print('output: ' + str(response))

    return response
