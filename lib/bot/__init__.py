import os
from glob import glob
from datetime import datetime

from discord import Intents
from discord.ext import commands

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

COGS = [path.split('\\')[-1][:-3].replace('./lib/cogs/','') for path in glob('./lib/cogs/*.py')]

class Bot(commands.Bot):
    def __init__(self,version) -> None:
        # Inherit
        super().__init__(command_prefix=PREFIX,help_command=None,intents=Intents.all())

        # New properties
        self.version = version

    def run(self) -> None:
        super().run(TOKEN)

    def setup(self) -> None:
        for cog in COGS:
            self.load_extension(f'lib.cogs.{cog}')

    def get_current_time(self) -> datetime:
        return datetime.now()

    """ BOT EVENTS """
    async def on_connect(self) -> None:
        self.setup()
        await self.wait_until_ready()
        print(f'CONNECTED at {self.get_current_time()} - The bot is connected !')

    async def on_ready(self) -> None:
        print(f'READY at {self.get_current_time()} - The bot is ready to work !')
    
    async def on_disconnect(self) -> None:
        print(f'DISCONNECTED at {self.get_current_time()} - The bot is disconnected !')