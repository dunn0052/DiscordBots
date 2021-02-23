# bot.py
import os
from Levenshtein import distance

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
IMAGES_PATH = os.getenv('IMAGES')
GIFS_PATH = os.getenv('GIFS')



bot = commands.Bot(command_prefix='!')


# EVENT HANDLERS
@bot.event
async def on_ready():
    print("T-800 : On")

async def findClosestCommand(command):
    topCommands = []

    for botCommand in bot.commands:
        topCommands.append((distance(command, botCommand.name), bot.command_prefix + botCommand.name))
    
    topCommands.sort(key = lambda cmd : cmd[0])

    return [c[1] for c in topCommands[:3]]

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        lev = await findClosestCommand(ctx.invoked_with)
        await ctx.send(f"Invalid command: Did you mean one of these? \r\n{', '.join(lev)}")
    else:
        raise error


# COMMAND HANDLERS

@bot.command(name='test', help='Testing bot messages')
async def test(ctx):
    await ctx.send("Who is your daddy and what does he do?!")

@bot.command(name='kill', help='Logg out bot')
async def kill(ctx):
    print("KILLING BOT")
    with open(os.path.join(GIFS_PATH, 'kill.gif'), 'rb') as f:
        killgif = discord.File(f)

    await ctx.send(file=killgif)
    await bot.logout()
    f.close()


# RUN
bot.run(TOKEN)

