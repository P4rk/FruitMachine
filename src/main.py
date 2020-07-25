import random
from time import sleep

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


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    if rolls > 100:
        await ctx.send('I only have 100 dice to roll...')
        sleep(1)
        await ctx.send('dickhead.')
        return
    if limit > 500:
        await ctx.send('Where you dropped as a baby,')
        await ctx.send(f'who has a {limit} sided dice?')
        if rolls > 1:
            sleep(1)
            await ctx.send(f'let alone {rolls} of them...')
        return


    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.loop.create_task(guild_icon_changer.icon_changer_task(bot))
bot.run(properties.TOKEN)
