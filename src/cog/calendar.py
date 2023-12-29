import logging
from discord.ext.commands import Cog, command
from cog.Base.Cog_Base import Cog_Base
import services.calendar as calendar_service

logger = logging.getLogger('discord.cog.calendar')


class CalendarCog(Cog_Base):
    def __init__(self, bot):
        super().__init__(bot)

    @command()
    async def event(self, ctx):
        events = await calendar_service.get()
        for event in events:
            await ctx.send(event["summary"])

    @Cog.listener()
    async def on_ready(self):
        logger.info('ready')


async def setup(bot):
    await bot.add_cog(CalendarCog(bot))
