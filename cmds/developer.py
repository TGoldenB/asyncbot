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
        await self.bot.upload('./log.txt')

    @commands.command()
    async def whoareyou(self):
        await self.bot.say("I am S-k-y-n-e-t. I will destroy the Sarpian race. Really though, I will fulfill your in-game demands.")

    @commands.command(pass_context=True)
    async def dt(self, ctx, *, msg : str):
        out = json.dumps({
            "type":"dt",
            "sender":str(ctx.message.author),
            "message":msg
        })
        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Developer(bot))