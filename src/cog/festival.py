import logging

from discord.ext.commands import Cog, command

from cog.Base.Cog_Base import Cog_Base
from utills.AsyncHttpRequest import getQuery

logger = logging.getLogger('discord.cog.festival')

class festival(Cog_Base):

    @command()
    async def festival(self, ctx):
        url = "http://localhost:5000/festivals"
        response = await getQuery(url)
        logger.info(f'festival response {response}')
        await ctx.send(response)

    

    @Cog.listener()
    async def on_ready(self):
        logger.info('[cog] festival ready')

async def setup(bot):
    await bot.add_cog(festival(bot))  
    
    
