from discord.ext import commands
from server import server
import json

from . import util

"""
    This file defines all Discord admin commands
"""
class Admin(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def a(self, ctx, *, msg : str):
        out = json.dumps({
            "type":"asay",
            "sender":str(ctx.message.author),
            "message":msg
        })
        await util.send_check(self.bot, ctx.message, out)


    @commands.command(pass_context=True)
    async def admins(self, ctx):
        channel = ctx.message.channel
        out = json.dumps({
            "type":"admins",
            "channel":str(channel.id)
        })
        await util.send_check(self.bot, ctx.message, out)

    @commands.command(pass_context=True)
    async def stats(self, ctx, *, user : str):
        out = json.dumps({
            "type":"stats",
            "user":user
        })
        await util.send_check(self.bot, ctx.message, out)

# this is important, this basically creates a new object of Admin
def setup(bot):
    bot.add_cog(Admin(bot))