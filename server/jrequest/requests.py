"""
    This is the file that initalizes all request types.
    You may import files declaring request types here.
    Do not clutter this file.
"""
from . request_type import get_types, request_type
from . import admin

import json
import discord
import time

channel = discord.Object(id='459193687398809600')

"""
    Defines a new request callback, test.
    This is invoked whenever a JSON request is received with a header,
    'type':'test'

    :param: server is the AServer object
    :param: data is in the form of JSON, that was passed to the server
"""
@request_type
async def a(server, data):
    
    text = str()
    for k in data:
        text += k + ":" + data[k] + "\n"
        
    await server.bot.send_message(channel, "Hello, I received your JSON request of type 'test';\n" + text)


@request_type
async def ping(server, data):
    
    text = data['author'] + " sent PING\nI say, PONG"
    await server.bot.send_message(channel, text)

@request_type
async def printtime(server, data):
    t = time.asctime(time.localtime(time.time()))
    await server.bot.send_message(channel, t)



