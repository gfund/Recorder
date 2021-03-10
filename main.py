from webs import keep_alive #webserver
import os #os manipulation
#DISCORD IMPORTS
###########################
import discord

import discord.ext
from discord.ext import commands
###############################


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
  #Debug Statement to Find the Current Working Directory (where the bot boots from(If you use this on your computer you should uncomment this and change line 44 to the path printed out since this was built to work on Repl.it not a personal computer))
  #cwd = os.getcwd()
  #print(cwd)
  print("Bot Booted")
  
@bot.command()
async def save(ctx,*mode):

  #if nothing or the server is put
  if mode=="()" or "server":
   if not os.path.exists(ctx.guild.name):
        os.makedirs(ctx.guild.name)
        os.chdir(ctx.guild.name)
      
        
   #go through text channels creating a text file with their history 

   for channel in ctx.guild.text_channels:
      f=open("{0}.txt".format(channel.name), "w+")
      messages = await channel.history().flatten()
      for message in messages:
       f.write(str(message.author)+" : "+message.content+"\n")
  #if channel is put

  elif mode=="channel":
        #save the text of a singular channel
        f=open("{0}.txt".format(ctx.channel.name), "w+")
        for message in messages:
         f.write(str(message.author)+" : "+message.content+"\n")
  #switch back to root path so that subdirectories are not created the next time the bot is run
  os.chdir("/home/runner/Recorder")
        
keep_alive()
#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)
