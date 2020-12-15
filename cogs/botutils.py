#
#           LineSMP BotUtils.py | 2020 :copyright: Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import BucketType
import traceback
from discord import Embed
import os
import datetime
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
class botutils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command(name="eval")
    @commands.is_owner()
    async def eval_(self, ctx, *, code):

        logs = self.bot.get_channel(788165731270262845)

        eval_embed = discord.Embed(
                title=f"{ctx.author.display_name} has used eval!", 
                description=f"""
**```css\n{code}!```**
                _ _
**Bot stats:**
Prefix: **{ctx.prefix}**
Bot: **{self.bot.user}**
Command executor: **{ctx.author}**
Guild: **{ctx.guild.name}**
                """, 
                timestamp=datetime.datetime.now(), 
                color=discord.Color.purple()
            )
        eval_embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        
        await logs.send(embed=eval_embed)

        code = code.strip("`")

        if code.startswith(("py\n", "python\n")):

            code = "\n".join(code.split("\n")[1:])
     
        try:

            exec(
                "async def __function():\n"
                + "".join(f"\n    {line}" for line in code.split("\n")),
                locals()
            )

            await locals()["__function"]()
        except Exception:

            res = Embed(
                title="its an error :(",
                description=f"```{traceback.format_exc()}```",
                color=discord.Colour.red()
            )
            res.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar_url_as(static_format="png")
            )

            await ctx.send(embed=res)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension = None): # extension arg

        if extension == None:

            embed = discord.Embed(title="Whoops!", description="_ _\n**You forgot to specify an extension to reload!**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=5)

        try:    
            
            logs = self.bot.get_channel(788165731270262845)

            embed = discord.Embed(title="Reloading!", description=f"_ _\n**```Reloading {extension}!```**\n_ _", color=discord.Color.dark_green())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=3)

            self.bot.reload_extension(extension)

            embed2 = discord.Embed(title="Reloaded!", description=f"_ _\n**```Reloaded {extension}!```**\n_ _", color=discord.Color.green())
            embed2.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            logs_embed = discord.Embed(
                title=f"{ctx.author.display_name} has reloaded an extension!", 
                description=f"""
**```css\nReloaded {extension}!```**
                _ _
**Bot stats:**
Prefix: **{ctx.prefix}**
Bot: **{self.bot.user}**
Command executor: **{ctx.author}**
Guild: **{ctx.guild.name}**
                """, 
                timestamp=datetime.datetime.now(), 
                color=discord.Color.purple()
            )
            logs_embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=embed2, delete_after=15)
            await logs.send(embed=logs_embed)
        
        except Exception as oops:

            embed = discord.Embed(title="Reloading error!", description=f"_ _\n**There was an error reloading - __{extension}__**!\n_ _\n**```{oops}```**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed, delete_after=30)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command()
    @commands.is_owner()
    async def botstatus(self, ctx, type = None, *, whatyadoin = None): 

        try:    
            
            logs = self.bot.get_channel(788165731270262845)

            embed = discord.Embed(title="Changing status!", description=f"_ _\n_ _", color=discord.Color.dark_green())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=3)
            

            if type == "dnd":

                await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=f"{whatyadoin}", type=discord.ActivityType.playing))

            elif type == "online":

                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=f"{whatyadoin}", type=discord.ActivityType.playing))

            embed2 = discord.Embed(title="Changed status!", description=f"_ _\n_ _", color=discord.Color.green())
            embed2.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            logs_embed = discord.Embed(
                title=f"{ctx.author.display_name} has changed the status!", 
                description=f"""_ _
Type: **{type}**
Content: **{whatyadoin}**
                _ _
**Bot stats:**
Prefix: **{ctx.prefix}**
Bot: **{self.bot.user}**
Command executor: **{ctx.author}**
Guild: **{ctx.guild.name}**
                """, 
                timestamp=datetime.datetime.now(), 
                color=discord.Color.purple()
            )
            logs_embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=embed2, delete_after=15)
            await logs.send(embed=logs_embed)
        
        except Exception as oops:

            embed = discord.Embed(title="Status error!", description=f"_ _\n**There was an error changing the status*!\n_ _\n**```{oops}```**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed, delete_after=30)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension = None): # extension arg

        if extension == None:

            embed = discord.Embed(title="Whoops!", description="_ _\n**You forgot to specify an extension to load!**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=5)

        try:    
            
            logs = self.bot.get_channel(788165731270262845)

            embed = discord.Embed(title="Loading!", description=f"_ _\n**```Loading {extension}!```**\n_ _", color=discord.Color.dark_green())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=3)

            self.bot.load_extension(extension)

            embed2 = discord.Embed(title="Loaded!", description=f"_ _\n**```Loaded {extension}!```**\n_ _", color=discord.Color.green())
            embed2.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            
            logs_embed = discord.Embed(
                title=f"{ctx.author.display_name} has loaded an extension!", 
                description=f"""
**```css\nLoaded {extension}!```**
                _ _
**Bot stats:**
Prefix: **{ctx.prefix}**
Bot: **{self.bot.user}**
Command executor: **{ctx.author}**
Guild: **{ctx.guild.name}**
                """, 
                timestamp=datetime.datetime.now(), 
                color=discord.Color.purple()
            )
            logs_embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=embed2, delete_after=15)
            await logs.send(embed=logs_embed)
        
        except Exception as oops:

            embed = discord.Embed(title="Loading error!", description=f"_ _\n**There was an error loading - __{extension}__**!\n_ _\n**```{oops}```**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed, delete_after=30)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.command()
    @commands.is_owner()
    async def sqleval(self, ctx, *, query: str):

        logs = self.bot.get_channel(788165731270262845)
        eval_embed = discord.Embed(
            title=f"{ctx.author.display_name} has used sqleval!", 
            description=f"""
**```css\n{query}```**
            _ _
**Bot stats:**
Prefix: **{ctx.prefix}**
Bot: **{self.bot.user}**
Command executor: **{ctx.author}**
Guild: **{ctx.guild.name}**
            """, 
            timestamp=datetime.datetime.now(), 
            color=discord.Color.purple()
        )
        eval_embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        
        await logs.send(embed=eval_embed)

        try:

            cursor = mydb.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            await ctx.send(result)

        except Exception as oops:

            embed = discord.Embed(title="SQL eval error!", description=f"_ _\n**There was an error**!\n_ _\n**```{oops}```**\n_ _", color=discord.Color.red())
            embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
            

def setup(bot):
    bot.add_cog(botutils(bot))
