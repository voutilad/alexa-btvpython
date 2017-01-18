"""
Ask Intent Fixtures
"""


def _base_intent():
    """
    Constructs a base intent object for constructing more specific intents
    :return: new dict
    """
    return {
        "version": "1.0",
        "session": {
            "sessionId": "SessionId.fc225185-356d-4801-9974-39346304b4ca",
            "application": {
                "applicationId": "amzn1.ask.skill.a1422305-89ad-4b1d-a730-409ec85bcc2b"
            },
            "attributes": {},
            "user": {
                "userId": "amzn1.ask.account.AGIBATV336BLB4OXENW5CEINYOPN6E6QVSVLH5MOIBVIHJOGRJBJFIXNSETUTBJ3LMO5YLLZZDJD6YOO3YQKTEQJAKQOM2JLIG2EEHTYBCLKSNZQNHMFLPPQJZP3O7NA6YS7F4UG5QLEQQGSDI3AMAYOF6J3GIBS7EHXTNWT2JCYUFWK5TU6AAQDQ7YI3ANFAWOAQBJEHYKQDPY"
            },
            "new": True
        }
    }


def new_launch_intent():
    return {u'session': {u'new': True, u'sessionId': u'amzn1.echo-api.session.d934894e-f3e1-4d23-960d-24b23cccf19e',
                         u'user': {
                             u'userId': u'amzn1.ask.account.AGIBATV336BLB4OXENW5CEINYOPN6E6QVSVLH5MOIBVIHJOGRJBJFIXNSETUTBJ3LMO5YLLZZDJD6YOO3YQKTEQJAKQOM2JLIG2EEHTYBCLKSNZQNHMFLPPQJZP3O7NA6YS7F4UG5QLEQQGSDI3AMAYOF6J3GIBS7EHXTNWT2JCYUFWK5TU6AAQDQ7YI3ANFAWOAQBJEHYKQDPY'},
                         u'application': {u'applicationId': u'amzn1.ask.skill.a1422305-89ad-4b1d-a730-409ec85bcc2b'}},
            u'version': u'1.0',
            u'request': {u'locale': u'en-US', u'timestamp': u'2017-01-17T14:51:36Z', u'type': u'LaunchRequest',
                         u'requestId': u'amzn1.echo-api.request.e75b58f4-e07a-4ccb-9bee-6e1b5c09e451'},
            u'context': {u'AudioPlayer': {u'playerActivity': u'PLAYING'},
                         u'System': {u'device': {u'supportedInterfaces': {u'AudioPlayer': {}}}, u'application': {
                             u'applicationId': u'amzn1.ask.skill.a1422305-89ad-4b1d-a730-409ec85bcc2b'}, u'user': {
                             u'userId': u'amzn1.ask.account.AGIBATV336BLB4OXENW5CEINYOPN6E6QVSVLH5MOIBVIHJOGRJBJFIXNSETUTBJ3LMO5YLLZZDJD6YOO3YQKTEQJAKQOM2JLIG2EEHTYBCLKSNZQNHMFLPPQJZP3O7NA6YS7F4UG5QLEQQGSDI3AMAYOF6J3GIBS7EHXTNWT2JCYUFWK5TU6AAQDQ7YI3ANFAWOAQBJEHYKQDPY'}}}}


def new_get_event_intent():
    return {
        "session": {
            "sessionId": "SessionId.4e3489c4-af45-4b5f-b00a-633c4bad60ab",
            "application": {
                "applicationId": "amzn1.ask.skill.a1422305-89ad-4b1d-a730-409ec85bcc2b"
            },
            "attributes": {},
            "user": {
                "userId": "amzn1.ask.account.AGIBATV336BLB4OXENW5CEINYOPN6E6QVSVLH5MOIBVIHJOGRJBJFIXNSETUTBJ3LMO5YLLZZDJD6YOO3YQKTEQJAKQOM2JLIG2EEHTYBCLKSNZQNHMFLPPQJZP3O7NA6YS7F4UG5QLEQQGSDI3AMAYOF6J3GIBS7EHXTNWT2JCYUFWK5TU6AAQDQ7YI3ANFAWOAQBJEHYKQDPY"
            },
            "new": True
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.0f5ab6f8-249c-4f3b-8ace-466550a9128f",
            "locale": "en-US",
            "timestamp": "2017-01-15T03:59:31Z",
            "intent": {
                "name": "GetNextEvent",
                "slots": {}
            }
        },
        "version": "1.0"
    }

mock_event = {
    'title': 'Mock Meeting',
    'date': 'Thursday, January 19',
    'venue': 'Miskatonic Universiy'
}