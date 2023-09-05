from src.faqbot import bot
from src.funcoes import separar, select, tem_faq
import asyncio


def configurar():
    @bot.command()
    async def faq(ctx, busca):
        busca = separar(busca)

        faq = select(busca)
        
        resposta = tem_faq(faq, busca)
        
        await asyncio.sleep(1) 

        await ctx.send(resposta)
