from discord.ext import commands
import discord

class CommandErrorHandler(commands.Cog): # class for all error handling
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.RoleNotFound):
            await ctx.send("Inputted role not found! Try again or use %help for more.")

        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found! Try again or use %help for more.")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing a required argument. Try again or use %help for more.")

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command entered does not exist. Type %help for more options.")

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))