from discord.ext import commands
import discord

class CommandErrorHandler(commands.Cog): # class for all error handling
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.send("Role not available on this server! Try again or use %help for more.")

        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found! Try again or use %help for more.")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing a required argument. Try again or use %help for more.")

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command entered does not exist. Type %help for more options.")

        if isinstance(error, commands.UserNotFound):
            await ctx.send("User could not be found! Try again or use %help for more.")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.mention} Command is on cooldown, please try again after {error.retry_after: .2f} seconds.')

        if isinstance(error, discord.HTTPException):
            await ctx.send("HTTP Error...")

        if isinstance(error, discord.errors.Forbidden):
            await ctx.send("I am missing permissions!")

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))