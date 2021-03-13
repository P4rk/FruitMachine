import glob
import random

import asyncio
import discord

import properties

_30_MINS_IN_SECONDS = 1800
_3_HOURS_IN_SECONDS = 7200


async def icon_changer_task(client: discord.Client):
    await client.wait_until_ready()
    while not client.is_closed:
        sleep = random.randint(_30_MINS_IN_SECONDS, _3_HOURS_IN_SECONDS)
        await icon_changer(client)
        await asyncio.sleep(sleep)


async def icon_changer(client: discord.Client):
    icon = pick_icon()
    with open(icon, 'rb') as file:
        bites = file.read()

    server = client.get_guild(id=properties.SERVER_ID)
    await server.edit(icon=bites)


def pick_icon() -> str:
    icons = glob.glob('src/images/guild-icons/*')
    icon_index = random.randint(0, len(icons)-1)
    return icons[icon_index]
