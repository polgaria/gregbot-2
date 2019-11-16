import discord
from discord.ext import commands
import os
import json

def server_prefix(greg, message):
    with open('prefixes.json', 'r') as prfx:
        prefixes = json.load(prfx)

    return prefixes[str(message.guild.id)]

greg = commands.Bot(command_prefix = server_prefix)
token = open('token', 'r').read()

@greg.event 
async def on_ready():
    guy = f'{greg.user.name} hates black people'
    print(guy)
    await greg.change_presence(activity=discord.Game('zsh'))

@greg.event
async def on_guild_join(guild):
     with open('prefixes.json', 'r') as prfx:
         prefixes = json.load(prfx)

     prefixes[str(guild.id)] = 'g!'

     with open('prefixes.json', 'w') as prfx:
         json.dump(prefixes, prfx, indent=4)

@greg.event
async def on_guild_remove(guild):
     with open('prefixes.json', 'r') as prfx:
         prefixes = json.load(prfx)

     prefixes.pop(str(guild.id))

     with open('prefixes.json', 'w') as prfx:
         json.dump(prefixes, prfx, indent=4)

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
