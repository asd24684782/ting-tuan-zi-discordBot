import logging

from discord.ext.commands import Cog, command

from cog.Base.Cog_Base import Cog_Base


logger = logging.getLogger('discord.cog.vote')

class Vote(Cog_Base):


    @Cog.listener()
    async def on_ready(self):
        logger.info('[cog] vote ready')


async def setup(bot):
    await bot.add_cog(Vote(bot))  
    
    
