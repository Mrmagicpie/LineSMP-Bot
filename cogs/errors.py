#
#           LineSMP errors.py | 2020 :copyright: Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):

            return

        elif isinstance(error,commands.NotOwner):
            rip_lmao = discord.Embed(
                description="<:smallx:770439044449566760> You do not have permission to use this!", 
                colour=discord.Colour.red(),
                timestamp=datetime.datetime.utcnow()
            )
            rip_lmao.set_footer(
                icon_url=self.bot.user.avatar_url,
                text="LineSMP "
            )
            return await ctx.send(embed=rip_lmao)

        elif isinstance(error,commands.CommandOnCooldown):

            c = round(error.retry_after)
            x = round(float("{:.2f}".format(error.retry_after)))
            days = int(c // 86400)
            hours = int(c // 3600)
            minutes = int(c // 60) 
            time = int(x)
            if time >= int(60):
                time = f"{minutes} minute(s)"
            elif minutes >= int(60):
                time = f"{hours} hour(s)"
            elif hours >= int(24):
                time = f"{days} day(s)"
            else:
                time = f"{x} second(s)"

            rip_lmao = discord.Embed(
                description=f"<:smallx:770439044449566760> You are on cooldown! Try again in {time}!", 
                colour=discord.Colour.red(),
                timestamp=datetime.datetime.utcnow()
            )
            rip_lmao.set_footer(
                icon_url=self.bot.user.avatar_url,
                text="LineSMP "
            )

            return await ctx.send(embed=rip_lmao)

        else:

            return await ctx.send(
                embed=discord.Embed(
                    title="Error! :x:", 
                    description=f"```css\n{error}\n```", 
                    color=discord.Color.red(),
                    timestamp=datetime.datetime.utcnow()
                ).set_footer(
                    icon_url=self.bot.user.avatar_url,
                    text="LineSMP "
                )
            ) # line.isthicc.xyz
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(errors(bot))
