import logging

from discord.ext.commands import Cog, command

from cog.Base.Cog_Base import Cog_Base
from config.config import get

config = get()
logger = logging.getLogger('discord.cog.system')


class System(Cog_Base):
    @command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @command()
    async def reload(self, ctx):
        for cog in config.system.cogs:
            await self.bot.reload_extension(f'cog.{cog}')
            logger.info(f'reload {cog}')

    @Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

    @Cog.listener()
    async def on_ready(self):
        logger.info('ready')


async def setup(bot):
    await bot.add_cog(System(bot))
