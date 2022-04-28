import discord

from discord.ext import commands

from .utils import parse_message

class SDK(commands.Cog):

    def __init__(self, client: discord.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        parsed = parse_message(self.client, message)
        if parsed and await self.client.is_owner(message.author):
            command, args = parsed
            await command(self.client, message, *args)

def setup(client: discord.Bot) -> None:
    client.add_cog(SDK(client))