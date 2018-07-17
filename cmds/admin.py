from discord.ext import commands
from discord import Member
from server import server
import json
import subprocess

from . import util

"""
    This file defines all Discord admin commands
"""
adminRoles = {
    "465874213324980244":"Administrator",
    "465896256972128266":"Junior",
    "465887716354031624":"General",
    "465896014130184192":"Senior",
    "465894668094144512":"Head",
    "465896094333927424":"Executive"
}

def is_admin(member : Member) -> str:
    for role in member.roles:
        if role.id in adminRoles:
            return adminRoles[role.id]


class Admin(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def a(self, ctx, *, msg : str):
        if not is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")

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
    async def prison(self, ctx,  player : str, ptime : int, *, reason : str):

        if not is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")
        out = json.dumps({
            "type":"prison",
            "sender":str(ctx.message.author),
            "player":player,
            "ptime": ptime,
            "reason": reason
        })
        await util.send_check(self.bot, ctx.message, out)

    @commands.command(pass_context=True)
    async def kick(self, ctx,  player : str, *, reason : str):
        
        if not is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")
        out = json.dumps({
            "type":"kick",
            "sender":str(ctx.message.author),
            "player":player,
            "reason": reason
        })
        await util.send_check(self.bot, ctx.message, out)


    @commands.command(pass_context=True)
    async def getlogs(self, ctx, pattern : str):
        cmd = ['grep', '-E', pattern, '/home/samp03/server_log.txt']
        with open('./files/log.txt', 'wb') as logf:
            subprocess.Popen(cmd, stdout=logf, shell=False) #shell=False to avoid shell injection
        await self.bot.upload('./files/log.txt')

    

    @commands.command(pass_context=True)
    async def kick(self, ctx,  player : str, *, reason : str):
        
        if not is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")
        out = json.dumps({
            "type":"kick",
            "sender":str(ctx.message.author),
            "player":player,
            "reason": reason
        })
        await util.send_check(self.bot, ctx.message, out)


    @commands.command(pass_context=True)
    async def w(self, ctx,  player : str, *, message : str):
        
        if not is_admin(ctx.message.author):
            return await self.bot.say("You are not an administrator.")
            
        out = json.dumps({
            "type":"w",
            "sender":str(ctx.message.author),
            "player":player,
            "message": message
        })
        await util.send_check(self.bot, ctx.message, out)
    """Temporary removing this
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
