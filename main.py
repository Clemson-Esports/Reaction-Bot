import json
import discord
import os
from discord.ext import commands
import discord_components
import ErrorHandling
import Reactions
import Help

with open('Bot_Secrets.json', 'r') as botSecrets:
    settings = json.load(botSecrets)
    TOKEN = settings['BotToken']

intents = discord.Intents.default()
intents.members = True

command_prefix = '%'
client = commands.Bot(intents=intents, command_prefix=command_prefix)

def addCog(client):
    ErrorHandling.setup(client)
    Reactions.setup(client)
    Help.setup(client)
    # LiveStreams.setup(client)

@client.event
async def on_ready(): # bot initialization
    discord_components.DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name="Go Tigers! | %help"))
    print(f'{client.user} has connected to Discord!')
    client.remove_command('help') # gets rid of default help command on bot

    addCog(client)  # adding all related cogs to the bot

client.run(TOKEN)