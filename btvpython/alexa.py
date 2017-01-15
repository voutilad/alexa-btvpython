"""
Our Alexa Skill for BTVPython
"""
from datetime import datetime
import os
import json
import urllib2

MEETUP_ENDPOINT = 'https://api.meetup.com/{group}/events?sign=false&key={key}&photo-host=public&page=1'

ASK_RESPONSE = {
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
        }
    },
    'shouldEndSession': True
}


def _convert_meetup_datetime(meetup_datetime):
    """
    convert the Meetup epoch datetime to a speakable version for Alexa
    :param meetup_datetime: epoch-based datetime
    :return: string of speakable datetime
    """
    fmt = '%A, %B %d'
    dt = datetime.fromtimestamp(int(meetup_datetime)/1000)
    return dt.strftime(fmt)


def get_next_meetup(group_name):
    """
    Lookup the next Meetup event for a group.
    :return: dict with details about the next event
    """
    meetup = {}

    url = MEETUP_ENDPOINT.format(group=group_name, key=os.environ['MEETUP_API_KEY'])
    response = json.loads(urllib2.urlopen(url).read())

    if response:
        meetup['title'] = response[0]['name']
        meetup['date'] = _convert_meetup_datetime(response[0]['time'])
        meetup['venue'] = response[0]['venue']['name']
    return meetup


def handle_intent():
    """
    Right now we'll just handle all intents as a request for the next meeting
    :return: message String
    """
    msg = 'The next Burlington Python meetup is "{title}" on {date} at {venue}'
    meetup = get_next_meetup('btvpython')
    if meetup:
        return msg.format(**meetup)
    else:
        return 'Sorry, I could not find an upcoming event for Burlington Python.'


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """
    if 'DEBUG_LAMBDA' in os.environ:
        print 'event: ' + str(event)
        print 'context: ' + str(context)


    output = ASK_RESPONSE.copy()
    message = handle_intent()
    output['response']['outputSpeech']['text'] = message
    output['response']['card']['content'] = message

    return output

