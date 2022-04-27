from typing import Tuple, List, Optional, Coroutine, Union
from discord import Message

from .shell import shell
from .eval import eval

CommandTypes = {
    'activate': 'activate',
    'deactivate': 'deactivate',
    'python': eval,
    'py': eval,
    'shell': shell,
    'sh': shell
}

def parse_message(client_id: int, message: str) -> Optional[Tuple[Union[Coroutine, str], List[str]]]:
    if message.startswith(f'<@{client_id}> '):
        message = message.replace(f'<@{client_id}> ', '', 1)
    elif message.startswith(f'<@!{client_id}> '):
        message = message.replace(f'<@!{client_id}> ', '', 1)
    else:
        return
    if command := CommandTypes.get(message.splitlines()[0].split(' ')[0].lower(), None):
        return (command, [arg for arg in message[len(message.splitlines()[0].split(' ')[0]):].split(' ')])