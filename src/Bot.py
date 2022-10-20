# -*- coding: UTF-8 -*- 
# Standard library imports
import logging
import asyncio
from glob import glob
from time import sleep

# Third party imports
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
# Local application imports
from cmds.cmds import test1, test2, test3
from setting.setting import DISCORD_TOKEN

logger = logging.getLogger('discord.Bot')
COGS = [path.split("\\")[-1][:-3] for path in glob("./cog/*.py")]


class Bot(commands.Bot):
    def __init__(self):
        logger.info('Bot init')
        self.PREFIX = commands.when_mentioned_or('.')
        self.TOKEN = DISCORD_TOKEN
        self.ready = False
        super().__init__(command_prefix=self.PREFIX, intents=discord.Intents.all())

    def run(self):
        super().run(self.TOKEN, reconnect=True)

    async def setup_hook(self):
        logger.info('set up hook')

        for cog in COGS:
            await self.load_extension(f'cog.{cog}')
            logger.info(f'{cog} cog load')

        self.addCmd(
            True,
            [test1, test2, test3]
        )

    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(1032215544608346185)
            logger.info(f'bot {self.user} is online')
            await self.stdout.send('我來了')
            self.ready = True

        else:
            logger.info('bot reconnected')

    async def on_connect(self):
        logger.info('bot connect')

    async def on_disconnect(self):
        logger.info('bot disconnect') 

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")

        else:
            await self.stdout.send('壞了')

    
    async def on_command_error(self, context, exception):
        if isinstance(exception, CommandNotFound):
            await context.send("wrong command")

        elif hasattr(exception, "orginal"):
            raise exception.original

        else:
            raise exception




    def addCmd(self, useful, cmdList):
        if useful:
            for cmd in cmdList:
                self.add_command(cmd)




bot = Bot()