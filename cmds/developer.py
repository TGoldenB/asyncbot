from discord.ext.commands import command, Context
import json

from . import util

"""
    This file defines all Discord developer commands
"""


class Developer(object):

    def __init__(self, bot):
        self.bot = bot

    @command(pass_context=True)
    async def dt(self, ctx: Context, *, msg: str):
        if not util.is_dev(ctx.message.author) and not util.is_tester(ctx.message.author):
            return await self.bot.say("You are not a developer.")

        out = json.dumps({
            "type": "dt",
            "sender": str(ctx.message.author.display_name),
            "message": msg
        })
        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Developer(bot))
