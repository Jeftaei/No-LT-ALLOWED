import json
import discord
import datetime

from discord.ext import commands, tasks
from discord.ext.commands.context import Context

losers = [276886193143152640, 425117122767618058]

with open("kicks.json", "r") as kjson:
    kicklog = json.load(kjson)
LaughableKicks = int(kicklog["kicks"])

with open("alts.json", "r") as altsjson:
    _altlist = json.load(altsjson)

class main(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self.kicks = LaughableKicks
        self.alts = _altlist["alts"]
        self.send_to_channel = 586631641619759194

        self.CountLaughablesKicks.start()

        print("main Cog Loaded")

    @tasks.loop(minutes=1)
    async def CountLaughablesKicks(self):
        with open("kicks.json", "w") as kjson2:
            json.dump( { "kicks" : self.kicks }, kjson2, indent=4 )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.id in self.alts: # laughable twister id
            await member.kick(reason="laughable :trollxd:")
        
            self.kicks += 1

            chnl = self.bot.get_channel(self.send_to_channel)
            await chnl.send(f"Laughable kick counter: {self.kicks}")

            print(f"Laughable kicked at {datetime.datetime.utcnow()}")

    @commands.command()
    async def addalt(self, ctx, member: discord.Member):
        if ctx.author.id in losers:
            if member.id not in self.alts:
                _altlist["alts"].append(member.id)
                with open("alts.json", "w") as ajson:
                    json.dump(_altlist, ajson, indent=4)
                
                # idk if i can read the files edited data right after i dumped shit into it
                with open("alts.json", "r") as ajson2:
                    self.alts = json.load(ajson2)["alts"]

                await member.kick(reason="new laughable alt Poggers :trollxd:")
                self.kicks += 1

                chnl = self.bot.get_channel(self.send_to_channel)
                await chnl.send(f"Laughable kick counter: {self.kicks}")

        



def setup(bot):
    bot.add_cog(main(bot))