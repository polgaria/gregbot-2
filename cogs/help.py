import discord
from discord.ext import commands

cog_name = 'Help'
class Help(commands.Cog):

    def __init__(self, greg):
        self.greg = greg

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')

def setup(greg):
    greg.add_cog(Help(greg))
