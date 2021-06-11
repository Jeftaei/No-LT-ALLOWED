import json
import discord
import datetime

from discord.ext import commands, tasks
from discord.ext.commands.context import Context

with open("kicks.json", "r") as kjson:
    kicklog = json.load(kjson)
LaughableKicks = int(kicklog["kicks"])

class main(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self.kicks = LaughableKicks

        self.CountLaughablesKicks.start()

        print("main Cog Loaded")

    @tasks.loop(seconds=5)
    async def CountLaughablesKicks(self):
        with open("kicks.json", "w") as kjson2:
            json.dump( { "kicks" : self.kicks }, kjson2, indent=4 )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.id == 365995444402126849: # laughable twister id
            await member.kick(reason="laughable :trollxd:")
            print("finished kicking")
        
        self.kicks += 1

        chnl = self.bot.get_channel(586631641619759194)
        await chnl.send(f"Laughable kick counter: {self.kicks}")

        print(f"Laughable kicked at {datetime.datetime.utcnow()}")



def setup(bot):
    bot.add_cog(main(bot))