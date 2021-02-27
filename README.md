# DiscordBots

Hello, this is dynamic loading discord bot T-800. It can hot load modules so you don't have to waste time reloading during development.

If you want to load the required modules you can do:

pip install -r requirements.txt

Or you can install the ones specified in requirements.txt individuslly. I don't care and it doesn't really matter.

To load in your own environment variables you will need to make a .env file and place it in srcPY

In there you need to specify some things

DISCORD_TOKEN=$YOUR DISCORD BOT TOKEN

GIFS=$Path to your gif folder starting from this root directory
IMAGES=$Same thing, but for your image folder
MODULES=$name of module folder followed by a period, I use 'module.' (Not surrounded by quotes)
