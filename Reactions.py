from discord.ext import commands
import discord
import emoji

class Reactions(commands.Cog, name= "Reactions"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        aliases=['rr'], invoke_without_command=True
    )
    @commands.guild_only()
    async def add_role(self, ctx, emoji, role=discord.Role):
        if role is None:
            await ctx.send("You did not give me a role to add!")
        else:
            emoji = emoji.emojize(emoji)
            print(emoji)


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
            print(role)
            description += f"{role}: {role.id}\n"

        print(roles)
        embed.description = description

        message = await channel.send(embed=embed)

        emojis = {
            '<:cursedsmile:569333374540316687>': 935751825477501018,
            '<:BUP:390351660028919808>': 2,
            '<:sunglassescry:635322510820376576>': 3

        }

        for i in range(0, len(emojis)):
            await message.add_reaction(list(emojis.keys())[i])


        await ctx.send("working...")

        # roled = discord.utils.get(ctx.guild.roles, name="rofl")
        # print(roled)


def setup(bot):
    bot.add_cog(Reactions(bot))