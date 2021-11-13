import json
import discord
import datetime
import time
import random

from discord.ext import commands, tasks

with open("json.json", "r") as stuff:
    stuff = json.load(stuff)

class main(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot

        self.kicks = stuff["kicks"]
        self.alts = stuff["accounts"]
        self.logChannel = 586631641619759194
        self.globalChannels = [769630756103913472, 771018473031073803, 769630324044070922, 771018378910892082, 769630228451819520] # globals, bhop-styles-globals, surf-styles-globals, bhop-auto-globals, surf-auto-globals

        print("main Cog Loaded")

    def SaveJson(self):
        with open("json.json", "w") as json2:
            json.dump( { "accounts": self.alts, "kicks": self.kicks }, json2, indent=4 )

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("Ready")
    #     # self.pingHiro.start()

    # check member on join and if the account id is in a list of known alts then it will kick him, update the number of kicks and send a message showing he was kicked
    # then it will update the json file holding the number of alts and kicks
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.id in self.alts:
            await member.kick(reason="laughable :trollxd:")
        
            self.kicks += 1

            chnl = self.bot.get_channel(self.logChannel)
            await chnl.send(f"Laughable kick counter: {self.kicks}")

            self.SaveJson()

    # this will add alts to the list of known alts to kick when they join
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def addalt(self, ctx, member: discord.Member):
        if member.id not in self.alts:
            self.alts.append(member.id)
            self.kicks += 1
            self.reloadjson()

            await member.kick(reason="new laughable alt :trollxd:")

            chnl = self.bot.get_channel(self.logChannel)
            await chnl.send(f"Laughable kick counter: {self.kicks}")
    
    # all this stuff thats commented is random shit i made for fun/just to fuck around, none of it is meant to be super good its just quickly wrote stuff

    @tasks.loop(seconds=1)
    async def pingeveryone(self):
        channel = self.bot.get_channel(self.logChannel)
        await channel.send("@everyone")

    @commands.Cog.listener()
    async def on_ready(self):
        self.pingeveryone.start()

    # probably a dumb way to do this but whatever, its all for jokes anyway
    # @tasks.loop(minutes=3)
    # async def pingHiro(self):
    #     rand = random.randint(1, 100)
    #     if rand >= 95:
    #         channel = self.bot.get_channel(self.logChannel)
    #         user = self.bot.get_user(263303913032253441)
    #         print(channel, user)
    #         msg = await channel.send(f"{user.mention}")
    #         await msg.delete(delay=0)
    #         random.seed( ((rand ** 5) / .5) * 7 )
    #         print(f"pinged hiro at {datetime.datetime.now()}")


    # thing i made really quickly to ping all the people with a certain role in a channel
    # probbaly made horribly, dont look to far into it
    # @commands.command()
    # @commands.is_owner()
    # async def pingeveryone(self, ctx, roleid: int, channelid: int):
    #     msg = ctx.message
    #     await msg.delete(delay=0)
        

    #     channel = self.bot.get_channel(channelid)
        
    #     members = channel.guild.get_role(roleid).members
    #     print(f"Members pinged = {len(members)}")

    #     message = ""

    #     for member in members:
    #         if len(message) > 1900:
    #             msg = await channel.send(message)
    #             await msg.delete(delay=0)
    #             message = ""
    #             time.sleep(2)
    #             print(f"\n\npinged inside (length = {len(message)})")

    #         message += member.mention
        
    #     if message:
    #         msg = await channel.send(message)
    #         await msg.delete(delay=0)
    #         print(f"\n\npinged outside (length = {len(message)})")


    # funny little thing to post last if the message in the channel is "last"
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author.bot == True:
    #         return 

    #     if message.channel.id == 874364230793564171 and "last" in message.content: # chanl
    #         await message.channel.send("last")
        
    # manual version of above
    # @commands.command()
    # @commands.is_owner()
    # async def say(self, ctx, channel):
    #     print(channel, self.bot.get_channel(int(channel)))
    #     channel = self.bot.get_channel(int(channel))
    #     await channel.send("last")
    #     await ctx.message.delete(delay=0)
    
    # funny thing to delete laughables globals because we thought it would b funny
    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.channel.id in self.globalChannels:
    #         try:
    #             field = message.embeds[0].fields[0]
    #             # print(field.name, field.value)
    #             if "player" in field.name.lower() and "laughabletwisty" in field.value.lower():
    #                 await message.delete(delay=0)
    #                 print(f"Deleted ({message.id}) at ({datetime.datetime.now()})\nTriggered by: ({field.name}, {field.value})")
    #         except Exception as e:
    #             # print("errored", e)


def setup(bot):
    bot.add_cog(main(bot))