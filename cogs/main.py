import json
import discord

from bot import bot as bott
from discord.ext import commands, tasks
from discord.ext.commands.context import Context

with open("kicks.json", "r") as kjson:
    kicklog = json.load(kjson)
LaughableKicks = int(kicklog["kicks"])
print(LaughableKicks)

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bott
        self.kicks = LaughableKicks

        self.CountLaughablesKicks.start()

        print("main Cog Loaded")

    @tasks.loop(seconds=5)
    async def CountLaughablesKicks(self):
        with open("kicks.json", "w") as kjson2:
            json.dump( { "kicks" : self.kicks }, kjson2, indent=4 )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.id == 365995444402126849: # laughable twister id
            member.kick(reason="laughable :trollxd:")
        
        self.kicks += 1
        

def setup(bot):
    bot.add_cog(main(bot))