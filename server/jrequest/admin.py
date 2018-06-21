from . request_type import get_types, request_type
import discord
import json

admin_chann = discord.Object(id='459193687398809600')

"""
    Admin chat
"""
@request_type
async def asay(server, data):
    embed = discord.Embed(title=data['player'], description=data['message'], color=0xFEB918)
    await server.bot.send_message(admin_chann, embed=embed)

@request_type
async def areport(server, data):
    embed = discord.Embed(title="Report from " + data['player'], description=data['message'], color=0xFFFF91)
    await server.bot.send_message(admin_chann, embed=embed)

@request_type
async def aann(server, data):
    embed = discord.Embed(title="Server Announcement", description=data['message'], color=0x58aecb)
    embed.set_footer(text=data['time'])
    await server.bot.send_message(admin_chann, embed=embed)

