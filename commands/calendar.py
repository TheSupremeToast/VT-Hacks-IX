from datetime import date
import discord, json, calendar
from discord.ext import commands

dayNumbers = ["M", "T", "W", "R", "F", "S", "U"]

#
# Class definition
#
class Calendar(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.hours = None

    # 
    # set_hours command
    # 
    @commands.command(name = 'set_hours')
    async def set_hours(self, ctx, *args):
        ret = ""

        initialized = False
        hours = get_saved_hours(ctx.author)
        for l in range(len(hours)):
            if(hours[l] != 0):
                initialized = True;
                break;
        for s in args:
                arg = s.split(":") # {MWF: 1400-1600}
                days = arg[0] # MWF
                times = arg[1]
                times = arg[1].split('-')
                time_start = times[0] # 1400
                time_end = times[1] # 1600 (}?)
                if(time_end < time_start):
                    await ctx.send("That's an invalid time")
                    return
                # [0,1,2,3,4,5,6]
                # [M,T,W,R,F,S,U]
                for i in range(len(days)): # dealing with one entry {MWF: 1400-1600}
                    index = -1;            # 0, 2, 4 -> {"time_start":1400, "time_end":1600}
                    for j in range(len(dayNumbers)):
                        if(days[i] is dayNumbers[j]):
                            index = j;
                            break;
                
                    hours[index] = {"time_start": time_start, "time_end":time_end};
        ta_hours = {"discord_name":ctx.author.display_name, "discord_id":ctx.author.id, "hours":hours};
        
        
        f = open("saved_hours.txt", 'r')
        lines = f.readlines();
        f.close()
        f = open("saved_hours.txt", 'w')
        for i in range(len(lines)):
            if(lines[i].find(str(ctx.author.id))==-1):
                f.write(lines[i])
        f.write(json.dumps(ta_hours) + '\n')
        f.close()

        await ctx.send(f"setting hours for {ctx.author.mention}");
    
    #
    # get_hours command
    #
    @commands.command(name = 'get_hours')
    async def get_hours(self, ctx):
        ret = ""
        num_printed = 0
        today = date.today()
        day = calendar.weekday(today.year, today.month, today.day);
        f = open("saved_hours.txt", 'r')
        for line in f:
            s = json.loads(line)
            hours = s['hours']
            if(hours[day]!=0):
                num_printed = num_printed + 1
                ret = ret + "**" + s['discord_name'] + "**" +  " has hours from " + str(hours[day]['time_start']) + " to " + str(hours[day]['time_end']) + '\n'
        if(num_printed==0):
            ret = ret + "No Hours Today\n"
        await ctx.send(ret)

    @commands.command(name = 'list_all_hours')
    async def list_all_hours(self, ctx):
        ret = ""
        week = ["","","","","","",""]
        num_printed = 0;
        f = open("saved_hours.txt", 'r')
        for line in f:
            s = json.loads(line)
            hours = s['hours']
            for i in range(len(week)):
                if(hours[i]!=0):
                    week[i] = week[i] + "**" + s['discord_name'] + "**" +  " has hours from " + str(hours[i]['time_start']) + " to " + str(hours[i]['time_end']) + '\n'
            ret = "Monday:\n" + week[0] + "Tuesday:\n" + week[1] + "Wednesday:\n" + week[2] + "Thursday:\n" + week[3] + "Friday:\n" + week[4] + "Saturday:\n" + week[5] + "Sunday:\n" + week[6]; 
        if(num_printed==0):
            ret = ret + "No Hours Today\n"

        embed = discord.Embed(color=discord.Color.from_rgb(99, 0, 49), title="TA Schedule", description=ret)
        
        await ctx.send(embed=embed)

# 
# Get previously saved hours for the given dicord ID
# 
def get_saved_hours(author_id):
    f = open("saved_hours.txt", "r");
    for line in f:
        if(line.find(str(author_id))>0):
            return json.loads(line)['hours']
    f.close()
    return [0]*7;



#
# Setup function: required for external commands file
#
def setup(client):
    client.add_cog(Calendar(client))