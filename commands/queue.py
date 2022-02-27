import discord
from discord.ext import commands

#
# Queue class to control queues for each class id
#
class Queue(commands.Cog):

    global queue
    queue = []

    def __init__(self, client):
        self.client = client
        # self.queue = [] 
    

    #
    # enter the queue
    #
    @commands.command()
    async def enqueue(self, ctx):
        queue.append(int(ctx.author.id)) 
        await ctx.send('You have entered the queue')
       

    #
    # command for TA's to run when they are done with a student
    #
    @commands.command()
    async def ta_available(self, ctx):
        user = dequeue(ctx)
        await ctx.send(f'See student <@{user}> now.')

    #
    # get the queue
    #
    @commands.command()
    async def get_queue(self, ctx):
        i = 0
        for user in queue:
            i += 1
            if int(user) == int(ctx.author.id):
                await ctx.send(f'You are in position {i} in queue.')


#
# remove user from queue and assign them to TA
#
def dequeue(ctx):
    try:
        next_student = queue.pop(0)
        return next_student
    except:
        return False

def setup(client):
    client.add_cog(Queue(client))
