from discord.ext import commands
from discord import Member
from server import server
import json

from . import util

"""
    This file defines all Discord admin commands
"""
devRole = "465874671733309440"
testerRole = "465874643337740290"

def is_dev(author : Member) -> bool:
    for role in author.roles:
        if role.id == devRole:
            return True
    return False

def is_tester(author : Member) -> bool:
    for role in author.roles:
        if role.id == testerRole:
            return True
    return False


class Developer(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whoareyou(self):
        await self.bot.say("I am S-k-y-n-e-t. I will destroy the Sarpian race. Really though, I will fulfill your in-game demands.")

    @commands.command(pass_context=True)
    async def dt(self, ctx, *, msg : str):

        if not is_dev(ctx.message.author) and not is_tester(ctx.message.author):
            return await self.bot.say("You are not a developer")

        out = json.dumps({
            "type":"dt",
            "sender":str(ctx.message.author.display_name),
            "message":msg
        })
        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Developer(bot))
