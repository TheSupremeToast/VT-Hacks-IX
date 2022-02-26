import discord
from discord.ext import commands

#
# Class definition
#
class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    #
    # example command setup
    #
    @commands.command(name = 'test')
    async def test(self, ctx):
        await ctx.send('test')

#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Example(client))
