#
#           LineSMP help.py | 2020 :copyright: Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
from discord import Embed as e
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command()
    @commands.cooldown(1, 3, type=BucketType.user)
    async def help(self, ctx):

        help = e(
            title="LineSMP Help",
            colour=discord.Colour.green(),
            timestamp=datetime.datetime.utcnow()
        )
        help.add_field(
            name="Uh-Oh Commands:",
            value="``;-;``\n``;=;``\n``;__=__;``"
        )
        help.set_footer(
            icon_url=self.bot.user.avatar_url,
            text="LineSMP "
        )

        await ctx.send(embed=help)

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(help(bot))
