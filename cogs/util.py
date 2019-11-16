import discord
from discord.ext import commands
import os
import json

cog_name = 'Util'
class Util(commands.Cog):

    def __init__(self, greg):
        self.greg = greg

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')

    @commands.command()
    async def setprefix(self, ctx, prefix):
        with open('./prefixes.json', 'r') as prfx:
            prefixes = json.load(prfx)

        prefixes[str(ctx.guild.id)] = prefix

        with open('./prefixes.json', 'w') as prfx:
            json.dump(prefixes, prfx, indent=4)

def setup(greg):
    greg.add_cog(Util(greg))
