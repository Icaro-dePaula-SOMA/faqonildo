import discord
from discord.ext import commands
# from discord_slash import SlashCommand 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)
# slash = SlashCommand(bot)
