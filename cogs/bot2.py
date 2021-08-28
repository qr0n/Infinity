import discord
import asyncio
import os
from asyncio import sleep as s  
import random
Vbl_loader = [
  "cogs.LV",
  "cogs.LV2"
]
sniped_messages = {}
from discord.ext import commands
import pyfiglet
class Commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["8ball", "8b"])
  async def _8ball(self, ctx, *, question):
	  responses = [
	     "It is certain.", "It is decidedly so.", "Without a doubt.",
	      "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
	      "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
	      "Reply hazy, try again.", "Ask again later.",
	      "Better not tell you now.", "Cannot predict now.",
	      "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	      "My sources say no.", "Outlook not so good.", "Very doubtful."
	  ]
	  await ctx.reply(
	      f"Your question was `{question}` And to that I say\n {random.choice(responses)}"
	  )

  @commands.command(aliases=["+", "plus"])
  async def add(self, ctx, left: int, right: int):
	  await ctx.send(left + right)


  @commands.command(aliases=["-", "subtract"])
  async def minus(self, ctx, left: int, right: int):
	  await ctx.send(left - right)


  @commands.command(aliases=["×", "multip"])
  async def multiply(self, ctx, left: int, right: int):
	  await ctx.send(left * right)

  @commands.command()
  async def divide(self, ctx, left : int, right:int):
    await ctx.send(left/right)

  @commands.command()
  async def ascii(self, ctx, *, text=None):
	  if text is None:
		  await ctx.send("You must input some text to make into Ascii!")
		  return
	  result = pyfiglet.figlet_format(text)

	  embed = discord.Embed(description=f"```{result}```")
	  await ctx.send(embed=embed)


  @commands.Cog.listener()
  async def on_message_delete(self, message):
	  sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

  @commands.command()
  async def snipe(self, ctx):
	  try:
		  contents, author, channel_name, time = sniped_messages[ctx.guild.id]

	  except:
		  await ctx.channel.send("Couldn't find a message to snipe!")
		  return

	  embed = discord.Embed(description=contents, color=discord.Color.blue(), timestamp=time)
	  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
	  embed.set_footer(text=f"Deleted in : #{channel_name}")

	  await ctx.channel.send(embed=embed)


  @commands.command()
  async def a(self, ctx, arg=None):
    await ctx.send("a_thing")
    
  @commands.Cog.listener()
  async def on_command_error(self,ctx, error):
    print(error)

  @commands.command()
  async def ranmem(self, ctx, member: discord.Member = None):
    await ctx.send(f"@{random.choice(ctx.guild.members)}")
  
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def pin(self, ctx, ID):
    message = await ctx.channel.fetch_message(ID)
    await message.pin()

  @commands.command()
  async def reminder(self, ctx, tme:int , *, msg):
    async with ctx.typing():

      author = ctx.author
    while True:
      await s(60*tme)
      embed = discord.Embed(title="Reminder", description=f"**{msg}** time of next reminder {tme} Minutes", colour=ctx.author.color, timestamp=ctx.message.created_at)
      await ctx.send(ctx.author.mention)
      await ctx.send(embed=embed)
      await author.send(embed=embed)

  @commands.command()
  async def tier(self, ctx, tm=10):
    while True:
      await s(1*tm)
      embed = discord.Embed(title="Timer", description=f"timer set for 10 min\n time remaining {tm}", color=ctx.author.color, timestamp=ctx.message.created_at)
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Commands(bot))
  print("VL is on")