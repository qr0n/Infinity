import discord
from discord.ext import commands

class Moderation(commands.Cog):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot
  
  
  # @commands.command()
  # @commands.has_permissions(manage_messages=True)
  # async def clear(self, ctx, amount=5):
  #   await ctx.send("cleared! <a:yes:793883148215779328>")
  
  # @commands.command()
  # @commands.has_permissions(kick_members=True)
  # async def kick(self, ctx, member: discord.Member, *, reason=None):
	#   await member.kick(reason=reason)

         
  # @commands.command()
  # @commands.has_permissions(ban_members=True)
  # async def ban(self, ctx, member: discord.Member, *, reason=None):
	#   ban_emb = discord.Embed(title=f"{member} was banned successfully", color=ctx.author.color)
	#   await member.ban(reason=reason)

    

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel: discord.TextChannel = None, *, Reason=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embedAAAAB = discord.Embed(title="Channel locked.🔒", description=f"Reason: ```md\n{Reason}```", color=0x3A56D4)
    await ctx.send(embed=embedAAAAB)

  @commands.command()
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