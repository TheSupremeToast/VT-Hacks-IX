import discord
from discord.ext import commands

#
# Class definition
#
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #
    # basic message embed
    #
    @commands.command(name = 'help')
    async def test(self, ctx):
        helpEmbed = discord.Embed(color=discord.Color.from_rgb(99, 0, 49), title='List of commands', description='List of commands for the bot')
        helpEmbed.add_field(name="queue", value="Queues you into your preferred office hours")
        helpEmbed.add_field(name="dequeue", value="Dequeues you out of your preferred office hours")
        helpEmbed.add_field(name="queuelist", value="Shows what position you are in your queue (if you're queued into one)")
        helpEmbed.set_footer(text="Type \"q! <command>\" if you want to use the bot")
        await ctx.send(embed=helpEmbed)
        

#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Help(client))