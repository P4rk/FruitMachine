import discord
from discord.ext import commands

import guild_icon_changer
import properties


description = '''
'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def playing(ctx, game: str):
    await bot.change_presence(activity=discord.Game(name=game))


@bot.command(pass_context=True)
async def icon(ctx):
    await guild_icon_changer.icon_changer(bot)


bot.loop.create_task(guild_icon_changer.icon_changer_task(bot))
bot.run(properties.TOKEN)
