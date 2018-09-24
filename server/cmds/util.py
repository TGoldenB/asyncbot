import discord
#  from itertools import islice
from server import server

"""
    This file contains helper functions, used in several command definitions for Discord.
"""


# Checks if the message was sent and adds feedback for the user
async def send_check(bot, message: discord.Message, data: str):
    sent = await server.get_server().write(data)
    if sent:
        await bot.add_reaction(message, '✅')
    else:
        await bot.add_reaction(message, '❌')


def get_log_chars():
    chars = []
    with open('server/files/log.txt', "r") as f:
        for char in f.read():
            chars.append(char)
    return len(chars)


def get_log_lines():
    num_lines = sum(1 for line in open('server/files/log.txt'))
    return num_lines


# def get_lines(lines: int):
#     with open('../files/log.txt', "r") as f:
#         head = list(islice(f, lines))
#     print(head)
