"""
A dictionary containing all the arguments for commands. Each cog loads their version and passes it through
to the commands using kwargs. The dictionary key name must be the same as the cog file name.

brief: Describes the command in !help
help: Message below the command in !help command
description: Message above the command in !help command
aliases: Alternate ways to invoke the command
pass_context: Passes a Context object as the first argument to the command
"""

commands = {

    # Player cog
    'player': {
        'whoareyou': {
            'brief': 'Who am I?',
            'help': 'USAGE: !whoareyou',
        },

        'id': {
            'brief': 'List player(s) containing the phrase or ID',
            'help': 'USAGE: !id <id/part_of_name>',
            'pass_context': True
        },

        'time': {
            'brief': 'Display the current server time',
            'help': 'USAGE: !time',
            'pass_context': True
        },

        'newb': {
            'brief': 'Send a message in /newb',
            'help': 'USAGE: !newb <message>',
            'pass_context': True
        }
    },

    # Admin cog
    'admin': {
        'a': {
            'brief': 'Send a message in /a',
            'help': 'USAGE: !a <message>',
            'pass_context': True
        },

        'admins': {
            'brief': 'List all online administrators',
            'help': 'USAGE: !admins',
            'pass_context': True
        },

        'prison': {
            'brief': 'Prison a player',
            'help': 'USAGE: !prison <id/name> <time(minutes)> <reason>',
            'pass_context': True
        },

        'getlogs': {
            'brief': 'Gather server logs of a specific pattern',
            'help': 'USAGE: !getlogs <pattern>',
            'description': 'Surround the pattern in quotation marks if there are spaces in the pattern',
            'aliases': ['gl'],
            'pass_context': True
        },

        'getbanreason': {
            'brief': 'Get the ban reason of a player',
            'help': 'USAGE: !getbanreason <firstname_lastname>',
            'aliases': ['gbr'],
            'pass_context': True
        },

        'kick': {
            'brief': 'Kick a player',
            'help': 'USAGE: !kick <id/name> <reason>',
            'pass_context': True
        },

        'w': {
            'brief': 'Whisper a player',
            'help': 'USAGE: !w <id/name> <message>',
            'pass_context': True
        }
    },

    # Developer cog
    'developer': {
        'dt': {
            'brief': 'Send a message in /dt',
            'help': 'USAGE: !dt <message>',
            'pass_context': True
        }
    }
}
