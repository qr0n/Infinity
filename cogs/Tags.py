import discord
from replit import db
from discord.ext import commands

class Dnds(commands.Cog, name='Per server tags'):
  '''These are the commands related to tag making'''
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  #@commands.has_permissions(manage_guild=True)
  async def add_tag(self, ctx, tag_name, *, tag_response):
    db[f"{ctx.guild.id}| {tag_name}"] = f"{tag_response}"
    await ctx.send("Tag added!")
  @commands.command()
  async def tag(self, ctx, tag):
    await ctx.send(db[f"{ctx.guild.id}|{tag}"])
  
  @commands.command()
  async def tags(self, ctx):   
    embed = discord.Embed(title="Guild tags.", description=db.prefix(f"{ctx.guild.id}|")[19:])
    await ctx.send(embed=embed)

  @commands.command()
  @commands.is_owner()
  async def alltags(self, ctx):
    await ctx.send(db.keys())

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def del_tag(self, ctx, tag):
    del db[f"{ctx.guild.id}|{tag}"]
    await ctx.send("Tags have been updated.")

    
def setup(bot):
  bot.add_cog(Dnds(bot))
  print("Tags: Loaded.")