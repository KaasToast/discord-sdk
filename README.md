# discord-sdk
A debug/utility extension for Discord bots. Made for Pycord.

## Installation
```
pip install git+https://github.com/KaasToast/discord-sdk/
```

## Usage
```py
import discord

INTENTS = discord.Intents.default(); INTENTS.message_content = True

client = discord.Bot(intents=INTENTS)

client.load_extension('discord-sdk')

client.run('TOKEN')
```