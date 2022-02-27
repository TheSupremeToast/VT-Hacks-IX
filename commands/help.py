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
        helpEmbed = discord.Embed(
            color=discord.Color.from_rgb(99, 0, 49), 
            title='Every command for our office hours queue bot', 
            description='List of commands for the bot'
        )
        helpEmbed.add_field(name="enqueue", value="Queues you into your preferred office hours")
        helpEmbed.add_field(name="get_queue", value="Shows what position you are in your queue (if you're queued into one)")
        helpEmbed.add_field(name="ta_available", value="Command for TAs to see the next person in queue")
        helpEmbed.add_field(name="set_hours", value="Command that lets the TA set their office hours")
        helpEmbed.add_field(name="get_hours", value="Shows you at what time TAs have office hours today")
        helpEmbed.add_field(name="list_all_hours", value="Lists all TA hours")
        helpEmbed.set_footer(text="Type \"q! <command>\" to use the bot!")
        await ctx.send(embed=helpEmbed)
        

#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Help(client))