# Dank memes
import discord
from discord.ext import commands
from requests import get
import json

client = commands.Bot(command_prefix="!")
@client.command()
async def hi(ctx):
   await ctx.reply("hi")
@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)
client.run("Token")