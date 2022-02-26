import discord
from discord.ext import commands

#
# Class definition
#
class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    #
    # basic message embed
    #
    @commands.command(name = 'embed')
    async def test(self, ctx):
        msg = discord.Embed(color=94008, title='embed', description='test embeds')
        await ctx.send(embed=msg)

#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Embed(client))