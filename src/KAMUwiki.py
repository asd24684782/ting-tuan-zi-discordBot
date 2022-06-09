# -*- coding: UTF-8 -*- 
import logging
from os import name
import yamlParser

import discord
import aioredis
from discord.ext import commands


#client connect Discord
#client = discord.Client()
client = commands.Bot(command_prefix='.')
#
logging.basicConfig(level=logging.INFO)

#ping
@client.command(name = "ping")
async def ping(ctx):
	await ctx.channel.send("pong")

#bot ready
@client.event
async def on_ready():
  print('bot', client.user, 'is online')
  game = discord.Game('動作和眼神不要太明顯')
  #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
  await client.change_presence(status=discord.Status.idle, activity=game)

#when get message
@client.event
async def on_message(message):
  #confirm not myself
  if message.author == client.user:
    return
  #如果以「說」開頭
  if message.content.startswith('說'):
    #分割訊息成兩份
    tmp = message.content.split(" ",2)
    #如果分割後串列長度只有1
    if len(tmp) == 1:
      await message.channel.send("你要我說什麼啦？")
    else:
      await message.channel.send(tmp[1])
  if message.content == '扶他小母牛屁眼塞炸彈':
    await message.channel.send('牛逼屌炸天')


if __name__ == '__main__':
  configDict = yamlParser.parser("../conf/config.yaml")
  token = configDict['token']
  #print(configDict['token'])
  client.run(token) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面