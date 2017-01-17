"""
Shared Meetup client logic
"""
import os
import requests
from datetime import datetime


MEETUP_ENDPOINT = 'https://api.meetup.com/{group}/events'


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

    params = {
        'key': os.environ['MEETUP_API_KEY'],
        'sign': False,
        'photo-host': 'public',
        'page': 1
    }
    response = requests.get(MEETUP_ENDPOINT.format(group=group_name), params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            meetup['title'] = data[0]['name']
            meetup['date'] = _convert_meetup_datetime(data[0]['time'])
            meetup['venue'] = data[0]['venue']['name']
    return meetup
