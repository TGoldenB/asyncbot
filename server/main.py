import discord
from discord.ext import commands
from server import server, settings
import sys, traceback, logging
import time

# import defined responses (response_type)
import requests

# import all defined commands in the cmds folder
cmd_files = [
    'cmds.admin',
    'cmds.developer',
    'cmds.player'
    ]


# setup the bot
description = """
Discord-SARP Connector\n
Author: dy1zan
Contributors: Gold, Kyle Young
"""
bot = commands.Bot(command_prefix='!', description=description, shard_count=10, max_messages=30)

if __name__ == '__main__':
    for extension in cmd_files:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load extension {1}." % extension, file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print('Connected to Discord')

    await bot.change_presence(status=discord.Status.do_not_disturb, game=discord.Game(name="Not connected"))

    # set profile pic
    #with open('media/profile_pic.png', 'rb') as f:
    #    await bot.edit_profile(avatar=f.read())

    # Assiocate the server with the bot
    server.get_server().set_bot(bot)
    # Start the server
    server.get_server().start()


while True:
    try:
        bot.loop.run_until_complete(bot.start(settings.BOT_TOKEN))
    except BaseException:
        time.sleep(2)
