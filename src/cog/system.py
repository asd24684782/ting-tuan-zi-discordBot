import logging

from discord.ext.commands import Cog, command

from cog.Base.Cog_Base import Cog_Base


logger = logging.getLogger('discord.cog.system')

class system(Cog_Base):

    @command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @command()
    async def load(self, ctx, cog):
        if cog == 'system':
            logger.info(f'[cog] can not load {cog}')
            await ctx.send(f'[cog] can not load {cog}')    
            return 

        await self.bot.load_extension(f'cog.{cog}')
        logger.info(f'[cog] load {cog}')
        await ctx.send(f'[cog] load {cog}')

    @command()
    async def unload(self, ctx, cog):
        if cog == 'system':
            logger.info(f'[cog] can not unload {cog}')
            await ctx.send(f'[cog] can not unload {cog}')    
            return

        await self.bot.unload_extension(f'cog.{cog}')
        logger.info(f'[cog] unload {cog}')
        await ctx.send(f'[cog] unload {cog}')

    @command()
    async def reload(self, ctx, cog):
        await self.bot.reload_extension(f'cog.{cog}')
        logger.info(f'[cog] reload {cog}')
        await ctx.send(f'[cog] reload {cog}')

    @Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        
    @Cog.listener()
    async def on_ready(self):
        logger.info('[cog] system ready')

async def setup(bot):
    await bot.add_cog(system(bot))  
    
    
