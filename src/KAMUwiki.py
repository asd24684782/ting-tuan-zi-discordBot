# -*- coding: UTF-8 -*- 
import discord

#client connect Discord
client = discord.Client()

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


    


client.run('OTI3OTI2MTMxMDMyNzM5ODYw.YdRUjQ.qQ_eoMbpc3rshztbwxf-9MgpDls') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面