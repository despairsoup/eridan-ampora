import os
from discord.ext import commands

bot = commands.Bot(command_prefix="eridan", case_insensitive=True)

bot.author_id = 487258918465306634


@bot.event
async def on_ready():  # When the bot is ready
    print("wwhy am i here with a bunch of land dwwellers")


extensions = [
    'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

token = os.environ.get("I_FUCKED_A_FISH")
bot.run