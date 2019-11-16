import discord
from discord.ext import commands

cog_name = 'ErrorHandler'
class ErrorHandler(commands.Cog):
    
    def __init__(self, greg):
        self.greg = greg

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{cog_name} was loaded.')
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Unknown command.')
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permissions required to run this command.')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Required argument "{}" is missing.')

        elif isinstance(error, commands.BadArgument):
            await ctx.send(error.args[0])
        else:
            await ctx.send('Unknown error.')

def setup(greg):
    greg.add_cog(ErrorHandler(greg))
