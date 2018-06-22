import discord
from discord.ext import commands
import asyncio
import server.server as server
import settings

#Request types
import requests

description = """
Discord-SARP Connector\n
Author: dy1zan
"""
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Connected to Discord')
    s = server.AServer(settings.SERVER_PORT, bot)
    s.start()



print(server)
bot.run(settings.BOT_TOKEN)