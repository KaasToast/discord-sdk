from discord import Bot, Message

async def shutdown(client: Bot, message: Message, *args) -> None:
    await message.add_reaction('👋')
    await client.close()