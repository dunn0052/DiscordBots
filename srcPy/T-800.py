# bot.py
import os
from Levenshtein import distance

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("T-800 : On")

@bot.event
async def on_command_error(error, ctx):


    if isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, "No such command")
    else:
        raise error

@bot.command(name='TEST', help='Testing bot messages')
async def TEST(ctx):
    await ctx.send("Who is your daddy and what does he do?!")

@bot.command(name='KILL', help='Logg out bot')
async def KILL(ctx):
    print("KILLING BOT")
    with open('kill.gif', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
    await bot.logout()

bot.run(TOKEN)

