import os
from src.comandos import configurar as config
from src.faqbot import bot


config()
bot.run(os.environ['BOT_FAQ_TOKEN']) 
