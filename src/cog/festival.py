from datetime import datetime
import logging

from discord.ext.commands import Cog, command
from discord import Embed

from cog.Base.Cog_Base import Cog_Base
from utills.AsyncHttpRequest import getQuery

logger = logging.getLogger('discord.cog.festival')
logger.setLevel(logging.INFO)

async def selectFestivalByID(id):
    logger.debug(f'select festival {id}')

    url = f"http://localhost:5000/festivals/id/{id}"
    response = await getQuery(url)
    logger.info(f'festival response {response}')

    code = response['code']
    message = response['message']
    festival = response['festival']

    id       = festival.get('id', "")
    name     = festival.get("name", "")
    location = festival.get("location", "")
    bands    = festival.get("bands", "")
    free     = festival.get("free", "")
    notes    = festival.get("notes", "")
    area     = festival.get("area", "")
    start    = festival.get("start", datetime.now())
    end      = festival.get("end", datetime.now())

    date = f'{start} ~ {end}' if start != end else start
    pay = '免費' if free else '要錢'
    bandStr = ""
    for band in bands:
        bandStr = bandStr + str(band) + "、"
    bandStr = bandStr[:-1]

    embedData = {
        "id"       : id,
        "name"     : name,
        "pay"      : pay,
        "area"     : area,
        "location" : location,
        "date"     : date,
        "bands"    : bandStr,
        "notes"    : notes,
    }

    return code, message, embedData

async def selectFestivalFree():
    logger.info('select festival is free')
        
    url = f"http://localhost:5000/festivals/free"
    response = await getQuery(url)
    logger.info(f'festival response {response}')

    code = response['code']
    message = response['message']
    festivals = response['festivals']

    return code, message, festivals

def makeDetailEmbed(embedData):
    logger.debug('make detail embed')

    title = str(embedData['id']) + '. ' + embedData['name']
    pay = embedData['pay']
    area = embedData['area']
    location = embedData['location']
    date = embedData['date']
    bands = embedData['bands']
    notes = embedData['notes']

    embed = Embed(title=title, description=pay, color=0xdd80ff)
    embed.add_field(name="地區",     value=area,     inline=False)
    embed.add_field(name="地點",     value=location, inline=False)
    embed.add_field(name="日期",     value=date,     inline=False)
    embed.add_field(name="演出人員",  value=bands,  inline=False)
    if notes != '':
        embed.add_field(name="備註", value=notes, inline=False)
    
    return embed


class festival(Cog_Base):

    @command(name='f')
    async def festival(self, ctx):
        url = "http://localhost:5000/festivals"
        response = await getQuery(url)
        logger.info(f'festival response {response}')
        await ctx.send(response)

        
    @command(name='fid')
    async def fid(self, ctx, id):
        logger.info(f'fid {id}')

        code, message, embedData = await selectFestivalByID(id)
        logger.info(f'select festival {id} done, embed Data = {embedData}')

        if code != '00':
            logger.warning(f'select festival {id} error {code}, {message}')
            await ctx.send(f'Error code {code}, {message}')
            return
        
        embed = makeDetailEmbed(embedData)
        logger.info(f'make embed done {embed}')

        await ctx.send(embed=embed)

    @command(name='ffree')
    async def festivalFree(self, ctx):
        logger.info('festival free')
        code, message, festivals = await selectFestivalFree()
        logger.info(f'select festival done, free festivals = {festivals}')

        if code != '00':
            logger.warning(f'select festival free error {code}, {message}')
            await ctx.send(f'Error code {code}, {message}')
            return

        embed = Embed(title="免費仔專屬", color=0xdd80ff)
        for f in festivals:
            name = str(f['id']) + '. ' + f['name']
            date = f['date']
            embed.add_field(name=name, value=date, inline=False)

        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        logger.info('[cog] festival ready')

async def setup(bot):
    await bot.add_cog(festival(bot))  
    
    
