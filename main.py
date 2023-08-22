import discord, asyncio, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

faqbot = commands.Bot(command_prefix='+', intents=intents)


async def start():
    await faqbot.start(os.environ['BOT_FAQ_TOKEN'])


asyncio.run(start())
