import discord
from discord.ext import commands
import asyncio
import server.server as server

description = """
Discord-SARP Connector\n
Author: dy1zan
"""
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Connected to Discord')
    s = server.AServer(6000, bot)
    s.start()



print(server)
bot.run('NDU5MTgyMDgwODMyNzAwNDE2.DgyeLw.KUhtSMWYimkn-Ud2hYB7csiYAMU')