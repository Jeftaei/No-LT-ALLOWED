import os
import json
import dotenv
import discord

from discord.ext import tasks, commands
_token = dotenv.dotenv_values()

intnets = discord.Intents.all()

bot = commands.Bot(command_prefix="fucklaughable", intents=intnets)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"Bot Online as '{bot.user}'")


bot.run(_token["token"], bot=True, reconnect=True)