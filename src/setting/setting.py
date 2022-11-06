import os
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
DISCORD_CHANNEL = int(os.getenv("DISCORD_CHANNEL"))
FESTIVAL_URL= os.getenv("FESTIVAL_URL")