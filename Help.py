from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command=None):
        channel = ctx.channel
        # cogs_desc = ''
        # for cog in self.bot.cogs:
        #     if self.bot.cogs[cog].__doc__ is not None: #ignores cogs without help descriptions
        #         cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

        if command is None:
            commands_desc = ''
            for command in self.bot.commands:
                if command != self.help:  # ignores help command
                    commands_desc += f'{command}, '

            print(commands_desc)

            embed = discord.Embed(title="Help Menu", description="Make sure to use the '%' prefix before entering a command!", color=0xF56600)
            embed.add_field(name="User Commands", value=f"```{commands_desc}```")
            await channel.send(embed=embed)

        else:
            """This is a temporary solution for help menu, faster method surely available."""
            commands_desc = ''
            for custom_command in self.bot.commands:
                if custom_command.name == command:  # ignores help command
                    commands_desc += f'{custom_command}, {custom_command.help}'

                    embed = discord.Embed(title="More Help",
                                          color=0xF56600)
                    embed.add_field(name=f"Help for {custom_command}", value=f"```{custom_command.help}```")
                    await channel.send(embed=embed)

            print(commands_desc)


def setup(bot):
    bot.add_cog(Help(bot))