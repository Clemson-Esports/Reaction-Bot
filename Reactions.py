from discord.ext import commands
import discord
from discord.utils import get

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dict = dict()

    @commands.group(
        aliases=['ar'], invoke_without_command=True
    )
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def add_role(self, ctx, emoji=None, role=None): # command for adding reactions to the react message
        """Call this command to add every role you want
        before creating the reaction message that you want to display.

        Usage: %add_role <:emoji:> <role>
        
        Attaches chosen emoji to chosen role (you may use either the role ID or name).
        This command is also callable by the alias: %ar """
        if emoji is None:
            await ctx.send("You forgot to enter an emoji! Try again or type %help for more options.")
        elif role is None:
            await ctx.send("You forgot to enter a role! Try again or type %help for more options.")
        else:
            try: # looks for role by id
                if not get(ctx.guild.roles, id=int(role)):
                    await ctx.send("Failed to find the inputted role. Try again or type %help for more options")
                else:
                    await ctx.send(f"Successfully added {emoji} to message!", delete_after=3)
                    self.dict[emoji] = role
                    return self.dict
            except: # looks for role by name
                if not get(ctx.guild.roles, name=role):
                    await ctx.send("Failed to find the inputted role. Try again or type %help for more options")
                else:
                    await ctx.send(f"Successfully added {emoji} to message!", delete_after=3)
                    self.dict[emoji] = role
                    return self.dict

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def listroles(self, ctx):
        """Simple command to list all available roles along with their equivalent ids [ Name : ID ]

        Usage: %listroles"""

        embed = discord.Embed(title="Reaction Roles!", color=0xF56600) #Clemson orange color for embed, of course
        channel = ctx.channel

        description = '[ Name : ID ] \n\n'
        roles = []
        for r in ctx.guild.roles:
            role = ctx.guild.get_role(r.id)
            roles.append(r)
            #print(role) #uncomment to print every role
            description += f"{role}: {role.id}\n"

        embed.description = description
        embed.add_field(name="More Info", value="You may use either the name or ID when adding a role"
                                                 " with the %add_role command!", inline=False)
        embed.add_field(name="More Help", value="For more help please visit:"
                                                " https://github.com/Clemson-Esports/Reaction-Bot", inline=False)
        await channel.send(embed=embed)

    @commands.group(
        aliases=['rm']
    )
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def reaction_message(self, ctx, description=None):
        """Call this command when all desired reaction roles have been created with %add_role.

        Usage: %reaction_message <'message'>

        As of right now, surrounding the desired message in quotations is needed if message is more than one word long
        This command is also callable by the alias: %rm"""

        channel = ctx.channel
        try:
            await channel.send("Testing that I can send messages in this channel...", delete_after=3)

            if description is None:  # makes sure user inputting command gives a description
                await ctx.send("No description was provided, try again or type %help for more options.")
                return
            else:
                description = description
                message = await ctx.channel.send(description)

                for i in range(0, len(self.dict)):
                    print("Adding Reactions to message...")
                    await message.add_reaction(list(self.dict.keys())[i])
        except:
            await ctx.send("I can not send messages in this channel, I am missing permissions!")
            return

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        emoji = payload.emoji
        print(emoji)
        guild = await self.bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        role = self.dict.get(str(emoji))
        #print(role)

        try:
            new_role = discord.utils.get(guild.roles, name=role)
            await member.add_roles(new_role)

        except:
            new_role = discord.utils.get(guild.roles, id=int(role))
            await member.add_roles(new_role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        emoji = payload.emoji
        #print(emoji)
        guild = await self.bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        role = self.dict.get(str(emoji))
        #print(role)

        try:
            new_role = discord.utils.get(guild.roles, name=role)
            await member.remove_roles(new_role)

        except:
            new_role = discord.utils.get(guild.roles, id=int(role))
            await member.remove_roles(new_role)

def setup(bot):
    bot.add_cog(Reactions(bot))