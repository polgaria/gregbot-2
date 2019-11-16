import discord
from discord.ext import commands
import os

greg = commands.Bot(command_prefix = 'g!')
token = open('token', 'r').read()

@greg.event 
async def on_ready():
    guy = f'{greg.user.name} hates black people'
    print(guy)
    await greg.change_presence(activity=discord.Game('zsh'))

@greg.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    greg.load_extension(f'cogs.{extension}')

@greg.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    greg.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        greg.load_extension(f'cogs.{filename[:-3]}')

greg.run(token.strip())
