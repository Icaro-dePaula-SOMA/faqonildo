import os
from src.comandos import configurar as config
from src.faqbot import bot


async def inicia():
    config()
    await bot.start(os.environ['BOT_FAQ_TOKEN'])

