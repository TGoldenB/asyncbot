import discord
from discord import Member
from server import server

"""
    This file contains helper functions, used in several command definitions for Discord.
"""

# Dictionary containing all command info, processed through kwargs.
commands = {
    # Player cog commands
    'player': {
        'whoareyou': {
            'brief': 'Who am I?',
            'help': 'USAGE: !whoareyou',
        },

        'newb': {
            'brief': 'Send a message in /newb.',
            'help': 'USAGE: !newb [message]',
            'pass_context': True
        }
    },

    # Admin cog commands
    'admin': {
        'a': {
            'brief': 'Send a message in /a.',
            'help': 'USAGE: !a [message]',
            'pass_context': True
        },

        'admins': {
            'brief': 'List all online administrators.',
            'help': 'USAGE: !admins',
            'pass_context': True
        },

        'prison': {
            'brief': 'Prison a player.',
            'help': 'USAGE: !prison [id/name] [time(minutes)] [reason]',
            'pass_context': True
        },

        'getlogs': {
            'brief': 'Gather server logs of a specific phrase.',
            'help': 'USAGE: !getlogs [phrase]',
            'descrption': 'Surround in "" if there are spaces in the phrase',
            'aliases': ['gl'],
            'pass_context': True
        },

        'kick': {
            'brief': 'Kick a player.',
            'help': 'USAGE: !kick [id/name] [reason]',
            'pass_context': True
        },

        'w': {
            'brief': 'Whisper a player.',
            'help': 'USAGE: !w [id/name] [message]',
            'pass_context': True
        }
    },

    # Developer cog commands
    'developer': {
        'dt': {
            'brief': '',
            'help': '',  # TODO: Add help info (unsure what this command does)
            'pass_context': True
        }
    }
}

admin_roles = {
    "465896094333927424": "Executive",
    "465894668094144512": "Head",
    "465896014130184192": "Senior",
    "465887716354031624": "General",
    "465896256972128266": "Junior",
    "475211931905556490": "Probie",
    "465874213324980244": "Administrator",
}

admin_ranks = {
    "Executive": 99999,
    "Head": 1337,
    "Senior": 4,
    "General": 3,
    "Junior": 2,
    "Probie": 1,
    "Administrator": 0
}

helper_role = "465874370904981514"
dev_role = "465874671733309440"
tester_role = "465874643337740290"


def is_admin(author: Member) -> str:
    highest = 0  # stores highest admin role
    highest_name = None  # stores highest admin role name

    for role in author.roles:
        if role.id in admin_roles:

            rank_name = admin_roles[role.id]
            rank = admin_ranks[rank_name]

            if rank > highest or highest is None:
                highest = rank
                highest_name = rank_name

    return highest_name


def has_role(author: Member, role_id: str) -> bool:
    for role in author.roles:
        if role.id == role_id:
            return True
    return False


# Checks if the message was sent and adds feedback for the user
async def send_check(bot, message: discord.Message, data: str):
    sent = await server.get_server().write(data)
    if sent:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')
