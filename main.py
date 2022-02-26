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

# load external extension files and remove help command
bot.remove_command('help')
load_cogs(bot)

#
# authenticate function to allow only admin users to use command
#
def authenticate(ctx):
    users = [os.getenv('PATRICK'), os.getenv('JAMES'), 
            os.getenv('GRADY'), os.getenv('MARCOS')]
    for user in users:
        if (int(ctx.author.id) == int(user)):
            return True
    return False

#
# define what to do when initially connected to discord
#
@bot.event
async def on_ready():
    print('Connected to discord.')

#####################################################

# Commands 

#
# Reload all external command files
#
@bot.command(name = 'reload_cogs')
async def reloadcogs(ctx):
    if (not authenticate(ctx)):
        await ctx.send('Insufficient Permissions.')
        pass
    try:
         reload_cogs(bot) 
         await ctx.send('Cogs reloaded.')
    except:
        await ctx.send('An error occured.')



# run the bot
bot.run(TOKEN)
