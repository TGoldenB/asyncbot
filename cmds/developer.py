from os.path import basename, splitext
from discord.ext.commands import command, Context
import json

from . import util
from .command_info import commands
from .constants import Section, Role


"""
    This file defines all Discord developer commands
"""

base_name = basename(__file__)
file_name = splitext(base_name)[0]
cog_commands = commands[file_name]


class Developer(object):

    def __init__(self, bot):
        self.bot = bot

    @command(**cog_commands['dt'])
    async def dt(self, ctx: Context, *, msg: str):
        if not Role.has_role(ctx.message.author, [Role.DEVELOPER, Role.TESTER]):
            return await self.bot.say("You are not a developer.")
        if not Section.in_section(ctx.message.channel.id, Section.DEVELOPMENT):
            return await self.bot.say("You must use this command in the _DEVELOPERS_ section.")

        out = json.dumps({
            "type": "dt",
            "sender": str(ctx.message.author.display_name),
            "message": msg
        })

        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Developer(bot))
