from typing import Tuple, List, Optional, Coroutine
from discord import Bot, Message

from .eval import eval
from .loading import load, unload, reload, cogs
from .shutdown import shutdown

CommandTypes = {
    'python': eval,
    'py': eval,
    'load': load,
    'ld': load,
    'unload': unload,
    'ul': unload,
    'reload': reload,
    'rl': reload,
    'shutdown': shutdown,
    'cogs': cogs
}

def parse_message(client: Bot, message: Message) -> Optional[Tuple[Coroutine, List[str]]]:
    if message.content.startswith(f'<@{client.user.id}> '):
        msg = message.content.replace(f'<@{client.user.id}> ', '', 1)
    elif message.content.startswith(f'<@!{client.user.id}> '):
        msg = message.content.replace(f'<@!{client.user.id}> ', '', 1)
    elif message.guild and message.content.startswith(f'<@&{message.guild.self_role.id}> '):
        msg = message.content.replace(f'<@&{message.guild.self_role.id}> ', '', 1)
    else:
        return
    command = CommandTypes.get(msg.splitlines()[0].split(' ')[0].lower(), None)
    args = [arg for arg in msg[len(msg.splitlines()[0].split(' ')[0]):].split(' ')]
    if len(args[0]) == 0: args = args[1:]
    if command:
        return (command, args)