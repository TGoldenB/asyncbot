from server.jrequest.request_type import request_type
import discord
import json

"""
    This file defines the output/style of bot messages,
    from requests received from the SA:MP server.
"""

# Stock/Default request types (ones that are reused)
@request_type
async def basic_player(server, data):
    #Set title (with player name appended), description and colour of the embed.
    embed = discord.Embed(title=data['title'] + " " + data['player'], description=data['message'], color=discord.Colour(int(data['color'])))
    #Set time as footer
    embed.set_footer(text=data['time'])
    #Send the embedded message to the specified channel
    await server.bot.send_message(discord.Object(id=data['channel']), embed=embed)

@request_type
async def basic(server, data):
    embed = discord.Embed(title=data['title'], description=data['message'], color=discord.Colour(int(data['color'])))
    embed.set_footer(text=data['time'])
    await server.bot.send_message(discord.Object(id=data['channel']), embed=embed)

@request_type
async def table(server, data):
    embed = discord.Embed(title=data['title'], description="Here is your response...", color=discord.Colour(int(data['color'])))

    lines = data['message'].split('\n')

    for line in lines:
        cols = line.split('\t')
        for col in cols:
            if(len(col) == 0): continue
            val = col.split('\r')

            embed.add_field(name=val[0], value=val[1], inline=True)

    embed.set_footer(text=data['time'])
    await server.bot.send_message(discord.Object(id=data['channel']), embed=embed)