"""
    Just a test file for now,
    future intention: define request types & invoke Discord API
"""
from request_type import get_types, request_type
import json


"""
    Defines a new request callback, test.
    This is invoked whenever a JSON request is received with a header,
    'type':'test'

    :param: server is the AServer object
    :param: data is in the form of JSON, that was passed to the server
"""
@request_type
async def test(server, data):
    await server.write("Hello, I received your JSON request of type 'test'; " + json.dumps(data))




