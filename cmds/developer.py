from discord.ext import commands
from server import server
import json

from . import util

"""
    This file defines all Discord admin commands
"""
class Developer(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def getlog(self, ctx):
        bot = server.get_server().bot
        await bot.type()
        await bot.upload('./log.txt')
        await bot.add_reaction(ctx.message, '✅')

# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Developer(bot))