from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        cogs_desc = ''
        for cog in self.bot.cogs:
            if self.bot.cogs[cog].__doc__ is not None: #ignores cogs without help descriptions
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

        commands_desc = ''
        for command in self.bot.commands:
            if command != self.help: #ignores help command
                commands_desc += f'`{command}` {command.help}\n'

        print(cogs_desc)
        print(commands_desc)

def setup(bot):
    bot.add_cog(Help(bot))