import os
from src.comandos import configurar as config
from src.faqbot import bot


async def inicia():
    config()
    # await bot.start(os.environ['BOT_FAQ_TOKEN']) # chave bot servidor SOMA
    await bot.start('MTE0NjEzNDUzOTMyOTA5Mzc4Mg.G-m2iI.ocvpFXxbUX1kvoQQh3bI7YlMM2W9qLZ4TAlXm8') # chave bot servidor do icaro
