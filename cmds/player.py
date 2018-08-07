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

    @command(**cog_commands['newb'])
    async def newb(self, ctx: Context, *, msg: str):
        if not Role.has_role(ctx.message.author, [Role.HELPER]) and not Role.get_admin_rank(ctx.message.author):
                return await self.bot.say("You are not a helper.")
        if ctx.message.channel.id != Channel.NEWBIE:
            return await self.bot.say("You must use this command in the #newbie channel.")

        out = json.dumps({
            "type": "newb",
            "sender": str(ctx.message.author.display_name),
            "message": msg
        })

        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Player(bot))
