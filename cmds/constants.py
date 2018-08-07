"""
Constants split into classes. Admin roles have extra information for rank comparison. Channels are combined into
lists in the Section class.

NOTE: This file can be accessed through importing util, which we do in every cog.
"""


class Role:
    # Admin roles have rank, id and level keys
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


class Channel:
    # IDs for every channel in the server

    # HELP/GENERAL
    GENERAL = 465873343518736397

    # ADMINISTRATORS
    DISCUSSION_ADMIN = 466404751857287178
    CHAT = 465873855672745985
    COMMANDS = 465875438321795074

    # HELPERS
    DISCUSSION_HELPER = 466420981813215232
    NEWBIE = 465874164960460800

    # PUBLIC SERVICES
    GOVERNMENT = 466434019278585869
    NEWS_AGENCY = 466434102661349380

    # DEVELOPMENT
    TESTERS = 465874413267582986
    CONFIRMED_BUGS = 471553508118626315
    BUGS = 465879591656095754
    BOT_TODO = 466949031898382356


class Section:
    # Lists of channel IDs for each section
    HELP_GENERAL: list[int] = [Channel.GENERAL]
    ADMINISTRATORS: list[int] = [Channel.DISCUSSION_ADMIN, Channel.CHAT, Channel.COMMANDS]
    HELPERS: list[int] = [Channel.DISCUSSION_HELPER, Channel.NEWBIE]
    PUBLIC_SERVICES: list[int] = [Channel.GOVERNMENT, Channel.NEWS_AGENCY]
    DEVELOPMENT: list[int] = [Channel.TESTERS, Channel.CONFIRMED_BUGS, Channel.BUGS, Channel.BOT_TODO]
