import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)