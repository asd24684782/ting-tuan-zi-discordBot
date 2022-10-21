from discord.ext.commands import Cog

class Cog_Base(Cog):
    def __init__(self, bot):
        self.bot = bot