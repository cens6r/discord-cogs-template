import discord, os, json

from discord.ext import commands
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "configurations\\.env")
load_dotenv(dotenv_path)

with open(os.path.join(os.path.dirname(__file__), "configurations\\config.json"), "r") as config:
    get = json.load(config)

prefix = get["prefix"]

intents = discord.Intents().all()
Client = commands.Bot(
    command_prefix=prefix, case_insensitive=True, intents=intents, help_command=None
)


@Client.command()
async def load(ctx, extension):
    try:
        Client.unload_extension(f"cogs.{extension}")
    except Exception:
        pass
    Client.load_extension(f"cogs.{extension}")
    e = discord.Embed(
        title=f"{extension} has been reloaded.", color=discord.Color.dark_green()
    )
    await ctx.reply(embed=e)


for filename in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\cogs"):
    if filename.endswith(".py"):
        Client.load_extension(f"cogs.{filename[:-3]}")

Client.run(os.environ.get("TOKEN"))
