from discord.ext import commands
from server import server
import json

from . import util

"""
    This file defines all Discord admin commands
"""
class player(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def newb(self, ctx, *, msg : str):
        out = json.dumps({
            "type":"newb",
            "sender":str(ctx.message.author),
            "message":msg
        })
        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(player(bot))