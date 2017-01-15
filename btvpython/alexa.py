"""
Our Alexa Skill for BTVPython
"""
import os
import json
import urllib2

MEETUP_ENDPOINT = 'https://api.meetup.com/{group}/events?sign=false&key={key}&photo-host=public&page=1'

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
        meetup['date'] = response[0]['time']
        meetup['venue'] = response[0]['venue']['name']
    return meetup


def lambda_handler(event, context):
    msg = 'The next Burlington Python meetup is "{title}" on {date} at {venue}'
    meetup = get_next_meetup('btvpython')
    if meetup:
        return msg.format(**meetup)
    else:
        return 'Sorry, I could not find an upcoming event for Burlington Python.'
