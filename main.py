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
bot = commands.Bot(command_prefix='!', description=description, shard_count=10, max_messages=30)
s = None

@bot.event
async def on_ready():
    print('Connected to Discord')
    global s
    s = server.AServer(settings.SERVER_PORT, bot)
    s.start()

# Checks if the message was sent and adds feedback for the user
async def send_check(message : discord.Message, data : str):
    sent = await s.write(data)
    if sent == True:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')

#These need moving to their own files where Discord commands are specified.
@bot.command(pass_context=True)
async def a(ctx, *, msg : str):
    out = json.dumps({
        "type":"asay",
        "sender":str(ctx.message.author),
        "message":msg
    })
    await send_check(ctx.message, out)


@bot.command(pass_context=True)
async def admins(ctx):
    channel = ctx.message.channel
    out = json.dumps({
        "type":"admins",
        "channel":str(channel.id)
    })
    await send_check(ctx.message, out)

@bot.command(pass_context=True)
async def stats(ctx, *, user : str):
    out = json.dumps({
        "type":"stats",
        "user":user
    })
    await send_check(ctx.message, out)

@bot.command(pass_context=True)
async def getlog(ctx):
    await bot.type()
    await bot.upload('./log.txt')
    await bot.add_reaction(ctx.message, '✅')



bot.run(settings.BOT_TOKEN)