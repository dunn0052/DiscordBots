# bot.py
import os
import importlib
from Levenshtein import distance

import discord
from dotenv import load_dotenv

from discord.ext import commands

from ModuleLoader import ModuleLoader

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
IMAGES_PATH = os.getenv('IMAGES')
GIFS_PATH = os.getenv('GIFS')


bot = commands.Bot(command_prefix='!')
mods = ModuleLoader()

# EVENT HANDLERS
@bot.event
async def on_ready():
    print("T-800 : On")

async def findClosestCommand(command):
    topCommands = []

    for botCommand in bot.commands:
        topCommands.append((distance(command, botCommand.name), bot.command_prefix + botCommand.name))
    
    topCommands.sort(key = lambda cmd : cmd[0])

    return [c[1] for c in topCommands[: min(len(topCommands), 3)]]

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Calculating Levenshtein edit distance...")
        lev = await findClosestCommand(ctx.invoked_with)
        await ctx.send(f"Did you mean one of these: \r\n{', '.join(lev)}")
    else:
        await ctx.send("Wat?")
        raise error


# COMMAND HANDLERS

@bot.command(name='test', help='Testing bot messages')
async def test(ctx):
    await ctx.send("Who is your daddy and what does he do?!")

''' Commenting this out so somneone who doesn't have a kill gif breaks this and wonders, wat m8? 
@bot.command(name='kill', help='Logg out bot')
async def kill(ctx):
    print("ASSASINATION ATEMPT!")
    if K_DAWG == ctx.author.id:

        with open(os.path.join(GIFS_PATH, 'kill.gif'), 'rb') as f:
            killgif = discord.File(f)

        await ctx.send(file=killgif)
        await bot.logout()
        f.close()
    else:
        await ctx.send(f"I’m sorry {ctx.message.author.display_name}, I’m afraid I can’t do that")

'''

@bot.command(name="load")
async def load(ctx, module):
    if(mods.reload_mod(module)):
        await ctx.send(f"Loaded {module} module")
    else:
        await ctx.send(f"YOU HAVE FAILED")

@bot.command(name="inject")
async def inject(ctx, module, func, *args):
    try:

        # get the furncion
        moduleFunction = mods.func_work(module, func)

        # verify args
        if mods.correctNumArgs(moduleFunction, args):
          
            # do work
            await moduleFunction(ctx, *args)
        else:
            await ctx.send("INCORRECT ARGS, DOLT")
    except:
        await ctx.send(f"YOU ARE INVALID")

# RUN
bot.run(TOKEN)

