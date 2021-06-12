import discord
from discord.ext import commands
import traceback
import sys


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.MemberNotFound):
            msg = await ctx.send(f"no member FOUND")
            await msg.delete(delay=10)

        elif isinstance(error, commands.BadArgument):
            msg = await ctx.send(f"Error: {error}")
            await msg.delete(delay=10)

        elif isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f'{error}')
            await msg.delete(delay=10)

        elif isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(f'{error}')
            await msg.delete(delay=10)

        elif isinstance(error, commands.errors.NotOwner):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            msg = await ctx.send(f"Hey! This command is on a cooldown. Please wait about `{round(error.retry_after, 2)}` more seconds!")
            await msg.delete(delay=5)

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))