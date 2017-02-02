"""
Tests for the Flask-version of the Skill
"""
import os
import json
from mock import patch
from btvpython.webapp import create_app, ASK_ROUTE
from .fixtures import new_launch_intent, new_get_event_intent, mock_event

os.environ['FLASK_SECRET_KEY'] = 'Testing'


class TestFlaskSkill(object):
    app = create_app()
    client = app.test_client()

    def setup_class(cls):
        cls.app.config['TESTING'] = True
        cls.app.config['ASK_VERIFY_REQUESTS'] = False

    def test_redirect_on_default_get(self):
        response = self.client.get('/', follow_redirects=False)
        assert response.status_code == 302
        assert response.location == 'https://github.com/voutilad/alexa-btvpython'



    def test_welcome_on_launch(self):
        post_data = json.dumps(new_launch_intent())
        response = self.client.post(ASK_ROUTE, data=post_data)
        assert response.status_code == 200

        response_json = json.loads(response.data)
        assert 'Welcome to Burlington Python' \
               in response_json['response']['outputSpeech']['text']
        assert 'You can say get next event or cancel' \
               in response_json['response']['reprompt']['outputSpeech']['text']

    @patch('btvpython.webapp.get_next_meetup', return_value=mock_event)
    def test_get_event_intent(self, mock):
        post_data = json.dumps(new_get_event_intent())
        response = self.client.post(ASK_ROUTE, data=post_data)
        assert response.status_code == 200

        response_json = json.loads(response.data.decode('utf-8'))
        speech = response_json['response']['outputSpeech']['text']
        assert mock_event['title'] in speech
        assert mock_event['venue'] in speech
        assert mock_event['date'] in speech
