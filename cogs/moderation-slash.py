import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

guild_ids = [759474157330366506]

class Moderation(commands.Cog):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot
  
    @cog_ext.cog_slash(name="lock", guild_ids=guild_ids)
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None, *, Reason=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embedAAAAB = discord.Embed(title="Channel locked.🔒", description=f"Reason: ```md\n{Reason}```", color=0x3A56D4)
      await ctx.send(embed=embedAAAAB)

    @cog_ext.cog_slash(name="unlock", guild_ids=guild_ids)
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None, Reason=None):
	    channel = channel or ctx.channel
	    overwrite = channel.overwrites_for(ctx.guild.default_role)
	    overwrite.send_messages = None
	    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	    embedAAAAA = discord.Embed(title="Channel unlocked.🔓", color=0x3A56D4)
	    await ctx.send(embed=embedAAAAA)      

def setup(bot):
  bot.add_cog(Moderation(bot))
  print('Loaded!')