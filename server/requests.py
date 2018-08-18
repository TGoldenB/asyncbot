from server.jrequest.request_type import request_type
import discord
import json

"""
    This file handles data sent from the PAWN
    client, or any other type of client...

    An example JSON request (which my PAWN API handles for you):
    {
        "type":"basic",
        "title":"Hello World",
        "message":"How are you doing, World?",
        "color":"{SOME VALID COLOUR IN DECIMAL}",
        "time":"{SOME VALID UNIX TIMESTAMP}"
    }
"""


@request_type
async def basic_player(server, data):
    """
        Same as @request_type=basic, except the player's name is appended
        to the title.
    """
    embed = discord.Embed(
        title=data['title'] + " " + data['player'],
        description=data['message'],
        color=discord.Colour(int(data['color']))
    )
    embed.set_footer(text=data['time'])

    # send the output to the specified Discord channel
    await server.bot.send_message(
        discord.Object(id=data['channel']),
        embed=embed
    )

@request_type
async def basic(server, data):
    """
        This represents a basic Discord output format.
        A title, a message in a coloured box with the time
        in the footer.
    """
    embed = discord.Embed(
        title=data['title'],
        description=data['message'],
        color=discord.Colour(int(data['color']))
    )
    embed.set_footer(text=data['time'])

    # send the output to the specified Discord channel
    await server.bot.send_message(
        discord.Object(id=data['channel']),
        embed=embed
    )