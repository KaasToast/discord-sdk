import discord

from discord.ext import commands

from .utils import parse_message

class SDK(commands.Cog):

    def __init__(self, client: discord.Bot) -> None:
        self.client = client
        self.active = False

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        parsed = parse_message(self.client.user.id, message.content)
        if parsed and await self.client.is_owner(message.author):
            command, args = parsed
            if command == 'activate':
                if self.active:
                    await message.add_reaction(message, False)
                else:
                    self.active = True
                    await message.add_reaction('❌')
            elif command == 'deactivate':
                if self.active:
                    self.active = False
                    await message.add_reaction('✅')
                else:
                    await message.add_reaction('❌')
            else: # elif self.active
                await command(self.client, message, *args)

def setup(client: discord.Bot) -> None:
    client.add_cog(SDK(client))