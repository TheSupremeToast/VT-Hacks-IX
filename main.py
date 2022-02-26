import os
import discord
from discord.ext import commands
from cogs import *

from dotenv import load_dotenv
load_dotenv()

# bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# set command prefix
bot = commands.Bot(command_prefix = 'q! ')

load_cogs(bot)

#
# authenticate function to allow only admin users to use command
# 
# TODO
#
def authenticate(ctx):
    users = [os.getenv('PATRICK'), os.getenv('JAMES'), 
            os.getenv('GRADY'), os.getenv('MARCOS')]
    for user in users:
        if (int(ctx.author.id) == int(user)):
            return True

    return False # change to false when functionality is implemented

#
# define what to do when connected to discord
#
@bot.event
async def on_ready():
    print('Connected to discord.')



#
#
#
@bot.command()
async def reload_cogs(ctx):
    if (not authenticate(ctx)):
        await ctx.send('Insufficient Permissions.')
        pass
    
   try: 
        load_cogs(bot)
   except:
       await ctx.send('An error occured')
    
    
    



#
# Example for command structure
#
@bot.command()
async def example(ctx):
    await ctx.send('example')

# run the bot
bot.run(TOKEN)
