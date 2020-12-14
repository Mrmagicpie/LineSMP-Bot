#
#           LineSMP uhoh.py | 2020 :copyright: Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class uhoh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command(name="-;")
    @commands.cooldown(1, 3, type=BucketType.user)
    async def _anything(self, ctx):

        if ctx.prefix == ";":

            await ctx.send(';-;')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command(name="__=__;")
    @commands.cooldown(1, 3, type=BucketType.user)
    async def _o(self, ctx):

        if ctx.prefix == ";":

             await ctx.send(';__=__;')

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command(name="=;")
    @commands.cooldown(1, 3, type=BucketType.user)
    async def _n_o(self, ctx):

        if ctx.prefix == ";":

            await ctx.send(';=;')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(uhoh(bot))
