from discord import embeds
import requests
import discord
from discord.ext import tasks, commands
from datetime import date

class BdayACNH(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.last_birthday = None

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     self.check_birthday.start()

    # @tasks.loop(hours=24.0)
    # async def check_birthday(self):
    #     birthday_channel = self.bot.guilds[0].get_channel(804341367346167830)
    #     r = requests.get('https://acnhapi.com/v1/villagers/')
    #     villagers = r.json()

    #     current_day = date.today().strftime("%B %#dth")
    #     for v in villagers:
    #         current_villager = villagers[v]
    #         if current_villager['birthday-string'] == current_day:
    #             name = current_villager['name']['name-EUfr']
    #             img = discord.Embed().set_image(url=current_villager['image_uri'])
    #             await birthday_channel.send(content=f'Joyeux anniversaire à {name} !',embed=img)

def setup(bot):
    bot.add_cog(BdayACNH(bot))