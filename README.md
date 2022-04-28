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

## Command Reference

The prefix for the command is mentioning the bot or it's integration role. Commands can only be ran by the owner of the bot.

### Evaluating python code:
````
python <code>

py <code>

python
```py
<code>
```

py
```
<code>
```
````
This command allows you to run python code, codeblocks are automatically handled. Buttons are included for re-running and sending the code you used.

### Running shell commands:
```
sh <command>

shell <command>
```
Runs commands through shell. Buttons are included for re-running and sending the code you used.

### Shutting down the bot
```
shutdown
```
Gracefully shuts down the bot.

### Cog management
```
load <extension(s)>

unload <extension(s)>

reload <extension(s)>

cogs
```
(Un/re) -loads specified extension(s) seperated by spaces. Cogs shows all currently loaded cogs.