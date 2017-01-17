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
    intent = _base_intent()
    intent.update({
      "request": {
        "type": "LaunchIntent",
        "requestId": "EdwRequestId.35fdb36f-6321-466e-820a-a33a8b934de2",
        "locale": "en-US",
        "timestamp": "2017-01-15T03:35:33Z",
      },
    })
    return intent


def new_get_event_intent():
    intent = _base_intent()
    intent.update({
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.35fdb36f-6321-466e-820a-a33a8b934de2",
        "locale": "en-US",
        "timestamp": "2017-01-15T03:35:33Z",
        "intent": {
            "name": "GetNextEvent",
            "slots": []
        }
      },
    })
    return intent

