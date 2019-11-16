import discord
from discord.ext import commands

cog_name = 'Miscellaneous'
class Miscellaneous(commands.Cog):

    def __init__(self, greg):
        self.greg = greg
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')

    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        """Displays some info about the bot."""
        embed = discord.Embed(title='gregbot 2', description='A (useless) discord.py bot', colour=0xff0000)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/644896423355351050/4742758a125ceaea9e2895105f1a0451.png')
        embed.add_field(name='Source code', value='https://github.com/polgaria/gregbot-2')
        embed.set_footer(text=f'Response time: {self.greg.latency * 1000:.2f}ms')

        await ctx.send(embed=embed)

    @commands.command(aliases=['uy'])
    async def guy(self, ctx):
        """guy"""
        await ctx.send('guy')

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """Displays the bot's response time (latency)"""
        await ctx.send(f'Ping: {self.greg.latency * 1000:.2f}ms')

def setup(greg):
    greg.add_cog(Miscellaneous(greg))
