import json
import discord
import datetime

from discord.ext import commands, tasks

with open("json.json", "r") as stuff:
    stuff = json.load(stuff)

class main(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self.kicks = stuff["kicks"]
        self.alts = stuff["accounts"]
        self.send_to_channel = 586631641619759194

        self.updatejson.start()

        print("main Cog Loaded")

    def reloadjson(self):
        with open("json.json", "w") as json2:
            json.dump( { "accounts": self.alts, "kicks": self.kicks }, json2, indent=4 )

    @tasks.loop(minutes=5)
    async def updatejson(self):
        # sick task right?
        # the only reason for this is to update the kicks, 
        # i dont do it in the on_member_join function because i dont wanna open and close the file
        # several times in a short period of time
        self.reloadjson()

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.id in self.alts:
            await member.kick(reason="laughable :trollxd:")
        
            self.kicks += 1

            chnl = self.bot.get_channel(self.send_to_channel)
            await chnl.send(f"Laughable kick counter: {self.kicks}")

            print(f"Laughable kicked at {datetime.datetime.utcnow()}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def addalt(self, ctx, member: discord.Member):
        if member.id not in self.alts:
            self.alts.append(member.id)
            self.kicks += 1
            self.reloadjson()

            await member.kick(reason="new laughable alt Poggers :trollxd:")

            chnl = self.bot.get_channel(self.send_to_channel)
            await chnl.send(f"Laughable kick counter: {self.kicks}")

        

def setup(bot):
    bot.add_cog(main(bot))