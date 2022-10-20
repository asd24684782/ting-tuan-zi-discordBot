from discord.ext.commands import Cog

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Fun cog ready")

async def setup(bot):
    await bot.add_cog(Fun(bot))