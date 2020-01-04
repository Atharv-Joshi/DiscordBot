import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print("Dummy bot is ready")

@client.command()
async def Hi(ctx):
    await ctx.send(f"HEllo")


client.run("NjYyNjQ3MjU3MTE5NTg4MzYy.Xg9ArA.grE0m5imerdlRoHkcgFLYwLPwI4")