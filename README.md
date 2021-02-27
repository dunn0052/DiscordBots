# DiscordBots

Hello, this is dynamic loading discord bot T-800. It can hot load modules so you don't have to waste time reloading during development.

If you want to load the required modules you can do:

pip install -r requirements.txt

Or you can install the ones specified in requirements.txt individuslly. I don't care and it doesn't really matter.

To load in your own environment variables you will need to make a .env file and place it in srcPY

In there you need to specify some things

in a file called .env

------------------------

DISCORD_TOKEN=$YOUR DISCORD BOT TOKEN

GIFS=$Path to your gif folder starting from this root directory
IMAGES=$Same thing, but for your image folder
MODULES=$name of module folder followed by a period, I use 'module.' (Not surrounded by quotes)

--------------------------------

Then in your module folder denoted by whatever MODULE environment variable is
I have provided SAMPLE.py as a sample module to do stuff like add new functions that you want to do

But onece you get the bot loaded in discord you can load your own modules and run functions from them by doing somethin like this

!load SAMPLE

!inject SAMPLE SAMPLE_FUNC args_from_discord

and your bot should call SAMPLE_FUNC from SAMPLE.py with the args_from_discord argument

While it's running you can modify SAMPLE.py and reload it by simply calling !load again

!load SAMPLE

then call your new function

!inject SAMPLE new_function whatever_args_you_want