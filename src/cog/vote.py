import logging
from discord.ext.commands import Cog, command
from cog.Base.Cog_Base import Cog_Base
from services.vote import Vote

logger = logging.getLogger('discord.cog.vote')


class VoteCog(Cog_Base):
    def __init__(self, bot):
        super().__init__(bot)
        self.vote = Vote()

    @Cog.listener()
    async def on_ready(self):
        logger.info('ready')


async def setup(bot):
    await bot.add_cog(VoteCog(bot))
