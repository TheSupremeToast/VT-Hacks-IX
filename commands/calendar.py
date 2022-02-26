import discord
from discord.ext import commands

#
# Class definition
#
class Calendar(commands.Cog):
    def __init__(self, client):
        self.client = client

    #
    # example command setup
    #
    @commands.command(name = 'get_hours')
    async def example_command(self, ctx):
        await ctx.send('getting hours!')

#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Calendar(client))