import discord
from discord.ext import commands
import asyncio
import server.server as server
import settings
import json

#Request types
import requests

description = """
Discord-SARP Connector\n
Author: dy1zan
"""
bot = commands.Bot(command_prefix='!', description=description)
s = None

@bot.event
async def on_ready():
    print('Connected to Discord')
    global s
    s = server.AServer(settings.SERVER_PORT, bot)
    s.start()

@bot.command(pass_context=True)
async def a(ctx, *, msg : str):
    out = json.dumps({
        "type":"asay",
        "sender":str(ctx.message.author),
        "message":msg
    })
    global s
    await s.write(out)

@bot.command()
async def admins():
    out = json.dumps({
        "type":"admins"
    })
    global s
    await s.write(out)


bot.run(settings.BOT_TOKEN)