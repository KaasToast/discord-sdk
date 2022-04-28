from discord import Bot, Message, File
from subprocess import run, PIPE, STDOUT, Popen, check_output
from io import StringIO

from .views import CodeView

async def shell(client: Bot, message: Message, *args) -> bytes:
    code = ' '.join(args).strip()
    if code.startswith('```sh\n'): code = code.replace('```sh\n', '', 1)
    elif code.startswith('```shell\n'): code = code.replace('```shell\n', '', 1)
    elif code.startswith('```\n'): code = code.replace('```\n', '', 1)
    if code[::-1].startswith('```\n'): code = code[::-1].replace('```\n', '', 1)[::-1]
    process = run(code.split(' '), stdout=PIPE, stderr=STDOUT, shell=True)
    if process.returncode == 0:
        await message.add_reaction('✅')
    else:
        await message.add_reaction('❌')
    buffer = StringIO()
    buffer.write(process.stdout.decode('utf-8'))
    buffer.seek(0)
    await message.reply(file=File(buffer, 'output.log'), mention_author=False, view=CodeView(client, message, 'shell', *args))