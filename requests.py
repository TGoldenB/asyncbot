from server.jrequest.request_type import request_type
import discord
import json

admin_chann = discord.Object(id='459858359357538326')

"""
    Admin chat
"""
@request_type
async def asay(server, data):
    embed = discord.Embed(title=data['player'], description=data['message'], color=0xFEB918)
    embed.set_footer(text=data['time'])
    await server.bot.send_message(admin_chann, embed=embed)


"""
    Player reports
"""
@request_type
async def areport(server, data):
    embed = discord.Embed(title="Report from " + data['player'], description=data['message'], color=0xFFFF91)
    embed.set_footer(text=data['time'])
    await server.bot.send_message(admin_chann, embed=embed)


"""
    Server announcements
"""
@request_type
async def aann(server, data):
    print(data)
    embed = discord.Embed(title="Server Announcement", description=data['message'], color=0x58aecb)
    embed.set_footer(text=data['time'])
    await server.bot.send_message(admin_chann, embed=embed)
