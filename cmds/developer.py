from os.path import basename, splitext
from discord.ext.commands import command, Context
import json

from . import util

"""
    This file defines all Discord developer commands
"""

base_name = basename(__file__)
file_name = splitext(base_name)[0]
commands = util.commands[file_name]


class Developer(object):

    def __init__(self, bot):
        self.bot = bot

    @command(**commands['dt'])
    async def dt(self, ctx: Context, *, msg: str):
        if not util.has_role(ctx.message.author, [util.Role.DEVELOPER, util.Role.TESTER]):
            return await self.bot.say("You are not a developer.")
        if not util.in_section(ctx.message.channel.id, util.Channel.SECTION_DEV):
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
