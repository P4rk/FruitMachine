import discord


async def play(client: discord.Client, game: str):
    await client.change_presence(activity=client.Game(name=game))
