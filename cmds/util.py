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
            'brief': 'Send a message in /dt.',
            'help': 'USAGE: !dt [message]',
            'pass_context': True
        }
    }
}


class Role:
    EXECUTIVE = {'rank': 'Executive', 'id': 465896094333927424, 'level': 99999}
    HEAD = {'rank': 'Head', 'id': 465894668094144512, 'level': 1337}
    SENIOR = {'rank': 'Senior', 'id': 465896014130184192, 'level': 4}
    GENERAL = {'rank': 'General', 'id': 465887716354031624, 'level': 3}
    JUNIOR = {'rank': 'Junior', 'id': 465896256972128266, 'level': 2}
    PROBIE = {'rank': 'Probie', 'id': 475211931905556490, 'level': 1}
    ADMINISTRATOR = {'rank': 'Administrator', 'id': 465874213324980244, 'level': 0}
    ADMIN_ROLES = [EXECUTIVE, HEAD, SENIOR, GENERAL, JUNIOR, PROBIE, ADMINISTRATOR]

    HELPER = '465874370904981514'
    DEVELOPER = '465874671733309440'
    TESTER = '465874643337740290'


class Section:
    HELP_GENERAL = 465873343518736396
    ADMINISTRATORS = 465874309555027978
    HELPERS = 465874210707734530
    PUBLIC_SERVICES = 466433904480485383
    DEVELOPMENT = 465874366584979457


class Channel:
    # HELP/GENERAL
    GENERAL = 465873343518736397
    SECTION_GENERAL = [GENERAL]

    # ADMINISTRATORS
    DISCUSSION_ADMIN = 466404751857287178
    CHAT = 465873855672745985
    COMMANDS = 465875438321795074
    SECTION_ADMIN = [DISCUSSION_ADMIN,CHAT, COMMANDS]

    # HELPERS
    DISCUSSION_HELPER = 466420981813215232
    NEWBIE = 465874164960460800
    SECTION_HELPERS = [DISCUSSION_HELPER, NEWBIE]

    # PUBLIC SERVICES
    GOVERNMENT = 466434019278585869
    NEWS_AGENCY = 466434102661349380
    SECTION_PUBLIC = [GOVERNMENT, NEWS_AGENCY]

    # DEVELOPMENT
    TESTERS = 465874413267582986
    CONFIRMED_BUGS = 471553508118626315
    BUGS = 465879591656095754
    BOT_TODO = 466949031898382356
    SECTION_DEV = [TESTERS, CONFIRMED_BUGS, BUGS, BOT_TODO]


def is_admin(author: Member) -> str:
    level = 0  # stores highest admin level
    rank = None  # stores highest admin rank

    for role in author.roles:
        for admin_role in Role.ADMIN_ROLES:
            if role.id == admin_role['id']:
                if rank is None:
                    rank = admin_role['rank']

                if admin_role['level'] > level:
                    level = admin_role['level']
    return rank


def has_role(author: Member, role_id_list: list) -> bool:
    for role in author.roles:
        for role_id in role_id_list:
            if role.id == role_id:
                return True
    return False


def in_section(channel_id: str, section_list: list) -> bool:
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
