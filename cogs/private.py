import discord
from discord.ext import commands

cog_name = 'Private'
class Private(commands.Cog):

    def __init__(self, greg):
        self.greg = greg

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')

    @commands.command(hidden=True, aliases=['kill'])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send('Bye Mom !!!')
        await self.greg.logout()

def setup(greg):
    greg.add_cog(Private(greg))
