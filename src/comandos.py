from src.faqbot import bot
from src.funcoes import separar, select, tem_faq
import asyncio
# from discord import SelectOption


def configurar():
    @bot.command()
    async def faq(ctx, busca = ''):
        busca = separar(busca)

        faq = select(busca)

        resposta = tem_faq(faq, busca)

        await asyncio.sleep(1) 

        for i in range(0, len(resposta), 1800):
            parte = resposta[i:i + 1800]
            await ctx.send(parte)


    # @bot.slash_command()
    # async def teste(ctx, name:SelectOption(str, "Nome")):
        
    #     await ctx.respond("Por favor, insira seu input.")

       