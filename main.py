import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print (">>Bot is online<<")


@bot.event
async def on_menber_join(member):
    print(f'{member}join!')
        channel = bot.get_channel(1002114006351360040)
        await channel.send(f'{member}join!')

@bot.event
async def on_menber_join(member):
    print(f'{member}leave!')
        channel = bot.get_channel(1002114044783755264)
        await channel.send(f'{member}join!')


bot.run('')