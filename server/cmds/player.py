from os.path import basename, splitext
from discord.ext.commands import command, Context
import json

from . import util
from .command_info import commands
from .constants import Channel, Role

"""
    This file defines all Discord player commands
"""

base_name = basename(__file__)
file_name = splitext(base_name)[0]
cog_commands = commands[file_name]


class Player(object):

    def __init__(self, bot):
        self.bot = bot

    @command(**cog_commands['whoareyou'])
    async def whoareyou(self):
        await self.bot.say(
            "I am S-k-y-n-e-t. I will destroy the Sarpian race. Really though, I will fulfill your in-game demands.")

    @command(**cog_commands['time'])
    async def time(self, ctx: Context):
        channel = ctx.message.channel

        out = json.dumps({
            "type": "time",
            "channel": str(channel.id),
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['admins'])
    async def admins(self, ctx: Context):
        channel = ctx.message.channel

        out = json.dumps({
            "type": "admins",
            "channel": str(channel.id)
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['id'])
    async def id(self, ctx: Context, pattern: str):
        channel = ctx.message.channel

        out = json.dumps({
            "type": "id",
            "channel": str(channel.id),
            "pattern": pattern
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['newb'])
    async def newb(self, ctx: Context, *, message: str):
        author = ctx.message.author
        channel = ctx.message.channel

        if not Role.has_roles(ctx.message.author, [Role.HELPER]) and not Role.is_admin(author):
                return await self.bot.say("You are not a helper.")
        if channel.id != Channel.NEWBIE:
            return await self.bot.say("You must use this command in the #newbie channel.")

        out = json.dumps({
            "type": "newb",
            "sender": str(author.display_name),
            "message": message
        })

        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Player(bot))
