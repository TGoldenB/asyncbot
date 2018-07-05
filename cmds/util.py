import discord
from server import server

"""
    This file contains helper functions, used in several command
    definitions for Discord.
"""

# Checks if the message was sent and adds feedback for the user
async def send_check(message : discord.Message, data : str):
    bot = server.get_server().bot
    sent = await server.get_server().write(data)
    if sent == True:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')