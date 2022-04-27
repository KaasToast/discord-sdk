import discord

INTENTS = discord.Intents.default(); INTENTS.message_content = True

client = discord.Bot(intents=INTENTS)

client.load_extension('discord-sdk')

client.run('TOKEN')