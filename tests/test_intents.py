from skill import handler
from tests import new_request, context


def test_intent():
    request = new_request('MyIntent', {'SlotName': 'slot value'})
    response = handler(request, context)

    expected_response = 'Your intent was reached. My response is, "slot value".'
    assert expected_response in response['response']['outputSpeech']['ssml']
    assert expected_response in response['response']['reprompt']['outputSpeech']['ssml']
