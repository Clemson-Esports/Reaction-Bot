from discord.ext import commands
import discord

class Reactions(commands.Cog, name= "Reactions"):
    def __init__(self, bot):
        self.bot = bot
        self.dict = dict()
        # self.message = message

    @commands.group(
        aliases=['ar'], invoke_without_command=True
    )
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def add_role(self, ctx, emoji, role): # command for adding reactions to the react message
        """Call this command to add every role you want
        before creating the reaction message that you want to display.

        Usage: %add_role <:emoji:> <role>
        
        Attaches chosen emoji to chosen role (you may use either the role ID or name).
        This command is also callable by the alias: %ar """
        if role is None:
            await ctx.send("You did not give me a role to add!")
        elif emoji is None:
            await ctx.send("You did not give me an emoji to add!")
        else:
            print(role)
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
            # print(role) uncomment to print every role
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
    async def reaction_message(self, ctx, description):
        """Call this command when all desired reaction roles have been created with %add_role.

        Usage: %reaction_message <'message'>

        As of right now, surrounding the desired message in quotations is needed if message is more than one word long
        This command is also callable by the alias: %rm"""

        def convertTuple(tup):
            str = ' '.join(tup)
            return str

        channel = ctx.channel
        try:
            await channel.send("Testing that I can send messages in this channel...", delete_after=3)
        except:
            await ctx.send("I can not send messages in this channel, I am missing permissions!")
            return

        if description is None: # makes sure user inputting command gives a description
            await ctx.send("No description was provided, try again...")
            return
        else:
            description = description
            embed = discord.Embed(title="Reaction Roles!", description=convertTuple(description))
            message = await ctx.channel.send(description)

            for i in range(0, len(self.dict)):
                print("Adding Reactions to message...")
                await message.add_reaction(list(self.dict.keys())[i])


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