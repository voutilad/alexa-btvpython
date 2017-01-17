"""
Tests for the Flask-version of the Skill
"""
import os
from btvpython.webapp import create_app, ASK_ROUTE


os.environ['FLASK_SECRET_KEY'] = 'Testing'


class TestFlaskSkill(object):
    app = create_app()
    client = app.test_client()

    def setup_class(cls):
        cls.app.config['TESTING'] = True

    def test_welcome_on_launch(self):
        response = self.client.get(ASK_ROUTE)
        assert response.status_code == 200
        assert b'Welcome to Burlington Python' in response.data

