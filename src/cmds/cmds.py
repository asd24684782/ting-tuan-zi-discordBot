from discord.ext import commands

@commands.command()
async def test1(ctx):
    await ctx.send('test1')

@commands.command()
async def test2(ctx):
    await ctx.send('test2')

@commands.command()
async def test3(ctx):
    await ctx.send('test3')
