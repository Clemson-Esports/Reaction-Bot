import discord
import os
from discord.ext import commands
import discord_components
import random
import ErrorHandling
import Reactions

TOKEN = 'OTM1NTg0NjUyMDk2MzQwMDQ5.YfAxGw.JKQEl-arQwIeEZevkWPDWgDvIeU'
GUILD = 'SteppingBeast Discord'

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='%')

def addCog(client):
    ErrorHandling.setup(client)
    Reactions.setup(client)

@client.event
async def on_ready(): # bot initialization
    discord_components.DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name="Go Tigers! | %help"))
    print(f'{client.user} has connected to Discord!')
    print(f'{GUILD}\n')
    addCog(client)  # adding all related cogs to the bot


client.run(TOKEN)