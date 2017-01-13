"""
Tests for our Alexa Skill
"""
from btvpython import alexa


def test_lambda_handler():
    assert alexa.lambda_handler(None, None) == 'Hello World!'
