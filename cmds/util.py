import discord
from server import server

"""
    This file contains helper functions, used in several command
    definitions for Discord.
"""


adminRoles = {
    "465896094333927424":"Executive",
    "465894668094144512":"Head",
    "465896014130184192":"Senior",
    "465887716354031624":"General",
    "465896256972128266":"Junior",
    "465874213324980244":"Administrator", 
}

playerRoles = {
    "465874370904981514":"Helper"
}

def is_admin(member : Member) -> str:
    for role in member.roles:
        if role.id in adminRoles:
            return adminRoles[role.id]
    return False

def is_helper(member : Member) -> bool:
    for role in member.roles:
        if role.id in playerRoles:
            if playerRoles[role.id] == "Helper":
                return True
    return False

# Checks if the message was sent and adds feedback for the user
async def send_check(bot, message : discord.Message, data : str):
    sent = await server.get_server().write(data)
    if sent == True:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')
