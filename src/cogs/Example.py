import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self , Client):
        self.Client = Client

    @commands.command()
    async def helloworld(self , ctx):
        await ctx.send('Hello World!')
      
def setup(Client):
    Client.add_cog(Example(Client))
