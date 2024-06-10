import os
from src.comandos import configurar as config
from src.faqbot import bot


config()
# bot.run(os.environ['BOT_FAQ_TOKEN']) # chave bot servidor SOMA
bot.run(os.environ['BOT_ICARO']) # chave bot servidor do icaro
