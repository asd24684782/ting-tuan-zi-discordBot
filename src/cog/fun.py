import logging
import asyncio

from discord.ext.commands import Cog

logger = logging.getLogger('discord.cog.fun')


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        logger.info('fun cog ready')

async def setup(bot):
    await bot.add_cog(Fun(bot))