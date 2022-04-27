import discord
import traceback

from io import StringIO

class EvalView(discord.ui.View):

    def __init__(self, code: str, client: discord.Bot, message: discord.Message) -> None:
        super().__init__(timeout=None)
        self.code = code
        self.client = client
        self.message = message

    @discord.ui.button(style=discord.ButtonStyle.green, emoji='🔁')
    async def re_run(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        _code = "\n".join([f"    {line}" for line in self.code.splitlines()])
        try:
            exec(f'async def eval(client, message):\n{_code}')
            output = str(await locals()['eval'](self.client, self.message))
        except:
            output = traceback.format_exc()
        buffer = StringIO()
        buffer.write(output)
        buffer.seek(0)
        await interaction.response.send_message(file=discord.File(buffer, 'output.log'), ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.green, emoji='📝')
    async def show_code(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        buffer = StringIO()
        buffer.write(self.code)
        buffer.seek(0)
        await interaction.response.send_message(file=discord.File(buffer, 'code.log'), ephemeral=True)