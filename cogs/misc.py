import discord
from discord.ext import commands

cog_name = 'Miscellaneous'
class Miscellaneous(commands.Cog):

    def __init__(self, greg):
        self.greg = greg
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')

    @commands.command(aliases=['uy'])
    async def guy(self, ctx):
        await ctx.send('guy')

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f'Ping: {self.greg.latency * 1000:.2f}ms')

def setup(greg):
    greg.add_cog(Miscellaneous(greg))
