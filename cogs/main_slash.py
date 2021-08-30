import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

guild_ids = [759474157330366506]


class SlashReload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="load", guild_ids=guild_ids)
    @commands.is_owner()
    async def test(self, ctx: SlashContext, cog):
        print("joe")
        try:
            self.bot.load_extension(cog)
            msg = f"{cog[4:]} was loaded successfully"
        except Exception as E:
            msg = E
            embed = discord.Embed(title=f"Loaded {cog[3:]}", description=msg)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name='unload', guild_ids=guild_ids)
    @commands.is_owner()
    async def ul(self, ctx: SlashContext, cog):
        try:
            self.bot.unload_extension(cog)
            msg = f"{cog[4:]} was unloaded successfully"
        except Exception as E:
            msg = E
            embed = discord.Embed(title=f"Reloading {cog[3:]}",
                                  description=msg)
            await ctx.send(embed=embed)
    


def setup(bot):
    bot.add_cog(SlashReload(bot))
    print('loaded ' + __name__)
