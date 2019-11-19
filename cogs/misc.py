import discord
from discord.ext import commands
import random

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

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """Displays the bot's response time (latency)"""
        await ctx.send(f'Ping: {self.greg.latency * 1000:.2f}ms')

    @commands.command(aliases=['serverinfo', 'guildinfo'])
    async def server(self, ctx):
        """Displays some info about the current server the bot is in"""
        embed = discord.Embed(title=f'{ctx.guild.name}', description=ctx.guild.id)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='Members', value=ctx.guild.member_count)
        embed.add_field(name='Channels', value=len(ctx.guild.channels))
        embed.add_field(name='Owner', value=ctx.guild.owner)
        embed.add_field(name='Created on', value=ctx.guild.created_at)
        embed.set_footer(text=f"Server region is '{ctx.guild.region}'")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['uy'])
    async def guy(self, ctx):
        """guy"""
        await ctx.send('guy')

    @commands.command(aliases=['ay'])
    async def gay(self, ctx, *, name):
        """Checks if someone/something is gay or not"""
        gay = [f'{name} is gay!',
               f'{name} is not gay!']
        if name.lower() in ('duck', 'emptybox', 'fox', 'oatmealine', 'jill', 'jillarella', 'ladizi'):
            await ctx.send(f'{name} is trans!')
        elif name.lower() in ('discord'):
            await ctx.send(f'🖕{name}🖕 is super gay!')
        else:
            await ctx.send(random.choice(gay))

def setup(greg):
    greg.add_cog(Miscellaneous(greg))
