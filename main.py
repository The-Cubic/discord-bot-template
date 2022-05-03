import os
import json
import logging
import disnake
from disnake.ext import commands

#----------Logging----------
logger = logging.getLogger('disnake')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='disnake.log',
    encoding='utf-8',
    mode='w'
)
handler.setFormatter(
    logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    )
)
logger.addHandler(handler)

#----------Bot----------
if __name__ == '__main__':
    with open('./config.json') as f:
        config = json.load(f)

    bot = commands.Bot(
        command_prefix=config['prefixes'],
        intents=disnake.Intents.all(),
        guilds_id=[948735546040152094]
    )

    @bot.event
    async def on_ready():
        print(bot.user)

    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    bot.run(config['token'])
