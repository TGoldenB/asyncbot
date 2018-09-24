import json
import subprocess
import asyncio
from os.path import basename, splitext
from discord.ext.commands import command, Context

from . import util
from .command_info import commands
from .constants import Channel, Role, Section, RePattern

"""
    This file defines all Discord admin commands
"""

base_name = basename(__file__)
file_name = splitext(base_name)[0]
cog_commands = commands[file_name]


class Admin(object):

    def __init__(self, bot):
        self.bot = bot

    @command(**cog_commands['a'])
    async def a(self, ctx: Context, *, message: str):
        author = ctx.message.author
        channel = ctx.message.channel

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if not Section.in_sections(channel.id, [Section.ADMINISTRATORS]):
            return await self.bot.say("You must use this command in the _Administrators_ section.")

        out = json.dumps({
            "type": "asay",
            "sender": str(author.display_name),
            "message": message
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['prison'])
    async def prison(self, ctx: Context,  player: str, ptime: int, *, reason: str):
        author = ctx.message.author
        channel = ctx.message.channel

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if channel.id != Channel.COMMANDS:
            return await self.bot.say("You must use this command in the #commands channel.")

        out = json.dumps({
            "type": "prison",
            "sender": str(author.display_name),
            "player": player,
            "ptime": ptime,
            "reason": reason
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['getlogs'])
    async def getlogs(self, ctx: Context, pattern: str):
        author = ctx.message.author
        channel = ctx.message.channel
        rank = Role.get_rank(author)

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if channel.id != Channel.COMMANDS:
            return await self.bot.say("You must use this command in the #commands channel.")
        if rank is "Probie":
            return await self.bot.say("Probationary admins cannot use this feature.")

        cmd = ['grep', '-m 3000', '-E', pattern, '/home/sarp/samp03z/server_log.txt']
        with open('server/files/log.txt', 'wb') as logf:
            subprocess.Popen(cmd, stdout=logf, shell=False)  # shell=False to avoid shell injection
        await asyncio.sleep(2)

        if util.get_log_chars() == 0:
            return await self.bot.say("No logs found.")

        if util.get_log_lines() <= 10 and util.get_log_chars() < 1990:
            with open('server/files/log.txt', "r") as f:
                log_message = '```\n{}\n```.format(f.read())'
            return await self.bot.say(log_message)

        await self.bot.upload('server/files/log.txt')

    @command(**cog_commands['getbanreason'])
    async def getbanreason(self, ctx: Context, player: str):
        author = ctx.message.author
        channel = ctx.message.channel
        is_rp_name = RePattern.contains_pattern(RePattern.RP_NAME, player)

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if channel.id != Channel.COMMANDS:
            return await self.bot.say("You must use this command in the #commands channel.")
        if not is_rp_name:
            return await self.bot.say("Please use the format: Firstname_Lastname.")

        out = json.dumps({
            "type": "getbanreason",
            "name": player
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['kick'])
    async def kick(self, ctx: Context,  player: str, *, reason: str):
        author = ctx.message.author
        channel = ctx.message.channel

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if not Section.in_sections(channel.id, [Section.ADMINISTRATORS, Section.HELPERS]):
            return await self.bot.say("You must use this command in the _Administrators_ or _Helpers_ section.")

        out = json.dumps({
            "type": "kick",
            "sender": str(author.display_name),
            "player": player,
            "reason": reason
        })

        await util.send_check(self.bot, ctx.message, out)

    @command(**cog_commands['w'])
    async def w(self, ctx: Context,  player: str, *, message: str):
        author = ctx.message.author
        channel = ctx.message.channel

        if not Role.is_admin(author):
            return await self.bot.say("You are not an administrator.")
        if not Section.in_sections(channel.id, [Section.ADMINISTRATORS, Section.HELPERS]):
            return await self.bot.say("You must use this command in the _Administrators_ or _Helpers_ section.")

        out = json.dumps({
            "type": "w",
            "sender": str(author.display_name),
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
