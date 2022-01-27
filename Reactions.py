from discord.ext import commands
import discord
import emoji

class Reactions(commands.Cog, name= "Reactions"):
    def __init__(self, bot):
        self.bot = bot
        self.dict = dict()

    @commands.group(
        aliases=['rr'], invoke_without_command=True
    )
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def add_role(self, ctx, emoji, role): # command for adding reactions to the react message
        if role is None:
            await ctx.send("You did not give me a role to add!")
        elif emoji is None:
            await ctx.send("You did not give me an emoji to add!")
        else:
            print(role)
            await ctx.send(f"Successfully added {emoji} to message!", delete_after=3)
            self.dict[emoji] = role
            return self.dict


    @commands.group(
        aliases=['rchannel', 'r_channel']
    )
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def rr_channel(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.send("No channel was given, defaulting to this channel...")
        channel = channel or ctx.channel
        try:
            await channel.send("Testing that I can send messages in this channel...", delete_after=3)
        except:
            await ctx.send("I can not send messages in this channel, I am missing permissions!")
            return

        embed = discord.Embed(title="Reaction Roles!")

        description = ''
        roles = []
        for r in ctx.guild.roles:
            role = ctx.guild.get_role(r.id)
            roles.append(r)
            #print(role) uncomment to print every role
            description += f"{role}: {role.id}\n"

        #print(roles)
        #print(self.dict)

        embed.description = description
        message = await channel.send(embed=embed)

        for i in range(0, len(self.dict)):
            print("Adding Reactions to message...")
            await message.add_reaction(list(self.dict.keys())[i])


        await ctx.send("working...")


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        emoji = payload.emoji
        print(emoji)
        guild = await self.bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        role = self.dict.get(str(emoji))
        print(role)

        try:
            new_role = discord.utils.get(guild.roles, name=role)
            await member.add_roles(new_role)
        except:
            new_role = discord.utils.get(guild.roles, id=int(role))
            await member.add_roles(new_role)


def setup(bot):
    bot.add_cog(Reactions(bot))