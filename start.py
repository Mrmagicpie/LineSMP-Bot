#
#           LineSMP start.py | 2020 :copyright: Mrmagicpie
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord
import asyncio
from discord.ext import commands
import os
import datetime
from config import TOKEN
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
async def get_prefix(bot, message):
    prefixes = [";", "line ", "smp ", "linesmp "]
    return commands.when_mentioned_or(*prefixes)(bot, message)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
bot.remove_command('help')

os.environ["JIKASHU_NO_UNDERSCORE"] = "True"
os.environ["JIKASHU_HIDE"] = "True"
bot.load_extension('jishaku')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
for cog in os.listdir('cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f"cogs.{cog[:-3]}")
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
@bot.event
async def on_ready():

    print(f'''
|--------------------|
| Bot ready!         |
| Signed in as:      |
|    {bot.user}    |
|--------------------|
    ''')

    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(name="Still waking up 😒, hold on!",
                                                        type=discord.ActivityType.watching))

    login = discord.Embed(
        title=f"{bot.user} has been started!",
        colour=discord.Colour.green(),
        timestamp=datetime.datetime.utcnow()
    )
    login.set_footer(
        icon_url=bot.user.avatar_url,
        text="LineSMP "
    )
    channel = bot.get_channel(788165731270262845)
    await channel.send('<@424721524621180930>', embed=login)
    await asyncio.sleep(10)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Wars on LineSMP", type=5))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
bot.run(TOKEN)
