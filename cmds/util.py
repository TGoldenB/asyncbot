import discord
from discord import Member
from server import server

from .constants import *

"""
    This file contains helper functions, used in several command definitions for Discord.
"""


def get_admin_level(author: Member) -> int:
    """
    Returns the admin level of a Discord member or None if they are not an admin
    """
    level = -1  # level 0 is taken by the base role
    for role in author.roles:
        for admin_role in Role.ADMIN_ROLES:
            if role.id == admin_role['id']:
                if admin_role['level'] > level:
                    level = admin_role['level']
    if level < 0:  # If not an admin
        level = None
    return level


def get_admin_rank(author: Member) -> str:
    """
    Returns the rank name of a Discord member or None if they are not an admin
    """
    rank = None
    level = 0
    for role in author.roles:
        for admin_role in Role.ADMIN_ROLES:
            if role.id == admin_role['id']:
                if admin_role['level'] > level:
                    rank = admin_role['rank']
                    level = admin_role['level']
    return rank


def has_role(author: Member, role_id_list: list) -> bool:
    """
    Verifies a Discord member has any number of roles in a list
    """
    for role_id in role_id_list:
        has_current_role = False
        for role in author.roles:
            if role.id == role_id:
                has_current_role = True
        if not has_current_role:
            return False
    return True


def in_section(channel_id: str, section_list: list) -> bool:
    """
    Verifies a Discord message waas posted in the correct channel by taking in a list constant from
    the Section class, a list of channels in the Discord server
    """
    for section_channel_id in section_list:
        if channel_id == section_channel_id:
            return True
    return False


# Checks if the message was sent and adds feedback for the user
async def send_check(bot, message: discord.Message, data: str):
    sent = await server.get_server().write(data)
    if sent:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')
