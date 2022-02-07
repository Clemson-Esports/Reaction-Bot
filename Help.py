from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command=None):
        channel = ctx.channel

        if command is None: #checks if user only inputted help with no extra command
            commands_desc = ''
            for command in self.bot.commands:
                if command != self.help:  # ignores help command
                    commands_desc += f'{command}, '

            embed = discord.Embed(title="Help Menu", description="Make sure to use the '%' prefix before entering a command!", color=0xF56600)
            embed.add_field(name="User Commands", value=f"```{commands_desc}```")
            await channel.send(embed=embed)

        else: # checks which command user inputted and shows related help description
            """This is a temporary solution for help menu, faster method surely available."""
            commands_desc = ''
            command_found = False
            for custom_command in self.bot.commands:
                if custom_command.name == command:  # ignores help command
                    command_found = True
                    commands_desc += f'{custom_command}, {custom_command.help}'

                    embed = discord.Embed(title="More Help",
                                          color=0xF56600)
                    embed.add_field(name=f"Help for {custom_command}", value=f"```{custom_command.help}```")
                    await channel.send(embed=embed)
            if not command_found:
                await ctx.send(f"Failed to find help for '{command}'. Try again or type %help for more options.")

def setup(bot):
    bot.add_cog(Help(bot))