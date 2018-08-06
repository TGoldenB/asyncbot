from os.path import basename, splitext
from discord.ext.commands import command, Context
import json

from . import util

"""
    This file defines all Discord player commands
"""

base_name = basename(__file__)
file_name = splitext(base_name)[0]
commands = util.commands[file_name]


class Player(object):

    def __init__(self, bot):
        self.bot = bot

    @command(**commands['whoareyou'])
    async def whoareyou(self):
        await self.bot.say(
            "I am S-k-y-n-e-t. I will destroy the Sarpian race. Really though, I will fulfill your in-game demands.")

    @command(**commands['newb'])
    async def newb(self, ctx: Context, *, msg: str):
        if not util.has_role(ctx.message.author, util.Role.HELPER):
            if not util.is_admin(ctx.message.author):
                return await self.bot.say("You are not a helper.")

        out = json.dumps({
            "type": "newb",
            "sender": str(ctx.message.author.display_name),
            "message": msg
        })

        await util.send_check(self.bot, ctx.message, out)


# this is important, this basically creates a new object of Developer
def setup(bot):
    bot.add_cog(Player(bot))
