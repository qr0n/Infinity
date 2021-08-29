import discord
from discord.ext import commands

from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_ids = [G.id for G in self.bot.guilds]

    @cog_ext.cog_slash(name="test")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="Embed Test")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash(bot))