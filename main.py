import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Bot is online")

    bot.run('ODY1MTcyODMxMjU2MTgyODA0.GQt17A.8IFHhIXjSVia78Hgqu4EBgOiGhIXPcRtXJmX_Y')