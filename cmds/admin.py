from discord.ext.commands import command, Context
import json
import subprocess
import asyncio

from . import util

"""
    This file defines all Discord admin commands
"""


class Admin(object):

    def __init__(self, bot):
        self.bot = bot

    @command(pass_context=True)
    async def a(self, ctx: Context, *, msg: str):
        if not util.is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")

        out = json.dumps({
            "type": "asay",
            "sender": str(ctx.message.author.display_name),
            "message": msg
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(pass_context=True)
    async def admins(self, ctx: Context):
        channel = ctx.message.channel

        out = json.dumps({
            "type": "admins",
            "channel": str(channel.id)
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(pass_context=True)
    async def prison(self, ctx: Context,  player: str, ptime: int, *, reason: str):
        if not util.is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")

        out = json.dumps({
            "type": "prison",
            "sender": str(ctx.message.author.display_name),
            "player": player,
            "ptime": ptime,
            "reason": reason
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(pass_context=True)
    async def getlogs(self, ctx: Context, pattern: str):

        admin_level = util.is_admin(ctx.message.author)
        if admin_level is "Probie":
            return await self.bot.say("Probationary admins cannot use this feature.")
        if not admin_level:
            return await self.bot.say("You are not an administrator.")

        cmd = ['grep', '-m 3000', '-E', pattern, '/home/sarp/samp03z/server_log.txt']
        with open('./files/log.txt', 'wb') as logf:
            subprocess.Popen(cmd, stdout=logf, shell=False)  # shell=False to avoid shell injection

        await asyncio.sleep(2)
        await self.bot.upload('./files/log.txt')

    @command(pass_context=True)
    async def kick(self, ctx: Context,  player: str, *, reason: str):
        if not util.is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")

        out = json.dumps({
            "type": "kick",
            "sender": str(ctx.message.author.display_name),
            "player": player,
            "reason": reason
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(pass_context=True)
    async def w(self, ctx: Context,  player: str, *, message: str):
        if not util.is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")

        out = json.dumps({
            "type": "w",
            "sender": str(ctx.message.author.display_name),
            "player": player,
            "message": message
        })

        await util.send_check(self.bot, ctx.message, out)

    """ Temporarily removing this
    @commands.command(pass_context=True)
    async def stats(self, ctx, *, user : str):
        out = json.dumps({
            "type":"stats",
            "user":user
        })
        await util.send_check(self.bot, ctx.message, out)
    """


# this is important, this basically creates a new object of Admin
def setup(bot):
    bot.add_cog(Admin(bot))
