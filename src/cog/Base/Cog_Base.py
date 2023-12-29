from discord.ext.commands import Cog
from Bot import DiscordBot


class Cog_Base(Cog):
    def __init__(self, bot: DiscordBot):
        self.bot = bot
