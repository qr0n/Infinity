import discord
import os
import json
from discord.ext import commands, tasks
from threading import Thread
from replit import db
from keep_alive import keep_alive
from discord_slash import SlashCommand, SlashContext

#imports ^

intents = discord.Intents.default()
intents.members = True
intents.presences = True

#intents ^ 

def get_prefix(client, message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload = True)

bot.author_id = 578789460141932555

Initial_extentions = [
	'cogs.bot2',
  'cogs.Tags',
  'cogs.main_cog',
  'cogs.rtfm',
  'cogs.Moderation',
  #'cogs.weather',
  'cogs.main_slash',
]

if __name__ == '__main__':
  for extension in Initial_extentions:
    try:
      bot.load_extension(extension)
    except Exception as E:
      raise E
      
@bot.event
async def on_ready():
  print("Logged in.")

@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")
    

@bot.listen("on_guild_join")
async def am(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@bot.event
async def on_message(msg):

    try:
        if msg.mentions[0] == bot.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)] 

            await msg.channel.send(f"My prefix for this server is `{pre}`")

    except:
        pass
    await bot.process_commands(msg)

@tasks.loop(hours=1)
async def auto_update():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      try:
        bot.unload_extension(f'cogs.{filename[:-3]}')
        bot.load_extension(f'cogs.{filename[:-3]}')
      except Exception as E:
        print(E)
    else:
      print(f'Unable to load {filename[:-3]}')
    


auto_update.start()
keep_alive()
bot.run(os.environ['token'])