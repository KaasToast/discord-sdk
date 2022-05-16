import traceback

from discord import Bot, Message

async def load(client: Bot, message: Message, *args) -> None:
    successful = []
    failed = []
    for arg in [arg.replace('/', '.').replace('\\', '.') for arg in args]:
        try:
            client.load_extension(arg)
            successful.append(arg)
        except:
            failed.append(traceback.format_exc().splitlines()[-1].split(": ", 1)[1])
    if len(failed) == 0:
        await message.add_reaction('✅')
    else:
        await message.add_reaction('⚠️')
        successful = f'\n\n{", ".join(successful)} loaded succesfully.' if len(successful) > 0 else ''
        failed = "\n".join(failed)
        await message.reply(f'```\n{failed}{successful}\n```', mention_author=False)

async def unload(client: Bot, message: Message, *args) -> None:
    successful = []
    failed = []
    for arg in [arg.replace('/', '.').replace('\\', '.') for arg in args]:
        try:
            if arg == 'discord-sdk':
                failed.append('Extension \'discord-sdk\' cannot be unloaded.')
            else:
                client.unload_extension(arg)
                successful.append(arg)
        except:
            failed.append(traceback.format_exc().splitlines()[-1].split(": ", 1)[1])
    if len(failed) == 0:
        await message.add_reaction('✅')
    else:
        await message.add_reaction('⚠️')
        successful = f'\n\n{", ".join(successful)} unloaded succesfully.' if len(successful) > 0 else ''
        failed = "\n".join(failed)
        await message.reply(f'```\n{failed}{successful}\n```', mention_author=False)

async def reload(client: Bot, message: Message, *args) -> None:
    successful = []
    failed = []
    for arg in [arg.replace('/', '.').replace('\\', '.') for arg in args]:
        try:
            if arg == 'discord-sdk':
                failed.append('Extension \'discord-sdk\' cannot be reloaded.')
            else:
                client.reload_extension(arg)
                successful.append(arg)
        except:
            failed.append(traceback.format_exc().splitlines()[-1].split(": ", 1)[1])
    if len(failed) == 0:
        await message.add_reaction('✅')
    else:
        await message.add_reaction('⚠️')
        successful = f'\n\n{", ".join(successful)} reloaded succesfully.' if len(successful) > 0 else ''
        failed = "\n".join(failed)
        await message.reply(f'```\n{failed}{successful}\n```', mention_author=False)

async def register(client: Bot, message: Message, *args) -> None:
    await client.sync_commands()
    await message.reply('Registered commands.', mention_author=False)

async def cogs(client: Bot, message: Message, *args) -> None:
    cogs = '\n'.join(client.cogs.keys())
    await message.reply(f'```\n{cogs}\n```', mention_author=False)