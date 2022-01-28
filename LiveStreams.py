from discord.ext import commands
import discord

class LiveStreams(commands.cog):
    """Help for Twitch Cog"""
    def __init__(self,bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(LiveStreams(bot))