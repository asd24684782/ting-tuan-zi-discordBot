import os
from dotenv import load_dotenv
import logging
from dataclasses import dataclass, field
from glob import glob

logger = logging.getLogger()
load_dotenv()


@dataclass
class StystemConfig:
    cogs: list[str]


@dataclass
class DiscordConfig:
    token: str
    guild: str
    channel: str


@dataclass
class DBConfig:
    host: str
    user: str
    password: str
    port: str
    name: str


@dataclass
class Config:
    is_load: bool = False
    system: StystemConfig = field(init=False)
    discord: DiscordConfig = field(init=False)
    db: DBConfig = field(init=False)


config = Config()


def load():
    config.is_load = True
    config.system = StystemConfig(
        cogs=[path.split("\\")[-1][:-3] for path in glob("./cog/*.py")]
    )
    config.discord = DiscordConfig(
        token=os.getenv("DISCORD_TOKEN"),
        guild=os.getenv("DISCORD_GUILD"),
        channel=int(os.getenv("DISCORD_CHANNEL"))
    )

    config.db = DBConfig(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        name=os.getenv("DB_NAME"),
    )


def get() -> Config:
    if not config.is_load:
        load()
    return config
