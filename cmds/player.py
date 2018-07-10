from discord.ext import commands
from discord import Member
from server import server
import json

from . import util

"""
    This file defines all Discord admin commands
"""
playerRoles = {
    "465874370904981514":"Helper"
}

def is_helper(member : Member) -> bool:
    for role in member.roles:
        if role.id in playerRoles:
            if playerRoles[role.id] == "Helper":
                return True
    return False

class player(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def newb(self, ctx, *, msg : str):
        if not is_helper(ctx.message.author):
            return await self.bot.say("You are not a helper.")

        out = json.dumps({
            "type":"newb",
            "sender":str(ctx.message.author),
            "message":msg
        })
        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(player(bot))