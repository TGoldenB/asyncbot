import re
from discord import Member

"""
Constants split into classes. Admin roles have extra information for rank comparison. Channels are combined into
lists in the Section class.
"""


class Pattern:

    RP_NAME_PATTERN = re.compile("[A-Z][a-z]+_[A-Z].*")  # Capital, any amount of non cap, underscore, capital, anything

    @staticmethod
    def contains_pattern(pattern, phrase):
        contains = bool(re.search(pattern, phrase))
        return contains


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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
    HELP_GENERAL: list = [Channel.GENERAL]
    ADMINISTRATORS: list = [Channel.DISCUSSION_ADMIN, Channel.CHAT, Channel.COMMANDS]
    HELPERS: list = [Channel.DISCUSSION_HELPER, Channel.NEWBIE]
    PUBLIC_SERVICES: list = [Channel.GOVERNMENT, Channel.NEWS_AGENCY]
    DEVELOPMENT: list = [Channel.TESTERS, Channel.CONFIRMED_BUGS, Channel.BUGS, Channel.BOT_TODO]

    @staticmethod
    def in_section(channel_id: str, section_list: list) -> bool:
        """
        Verifies a Discord message was posted in the correct channel by taking in a list constant from
        the Section class, a list of channels in the Discord server
        """
        for section_channel_id in section_list:
            if channel_id == section_channel_id:
                return True
        return False
