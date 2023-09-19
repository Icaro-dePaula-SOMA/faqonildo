from src.faqbot import bot
from src.funcoes import separar, select, tem_faq, vazia
import asyncio


def configurar():
    @bot.command()
    async def faq(ctx, busca = ''):
        if vazia(busca):
            await ctx.send('Sua pesquisa está vazia, tenta denovo por favor.')

        busca = separar(busca)

        faq = select(busca)

        resposta = tem_faq(faq, busca)

        await asyncio.sleep(1) 

        for i in range(0, len(resposta), 1800):
            parte = resposta[i:i + 1800]
            await ctx.send(parte)


    # @slash.slash(name="sla", description="Teste 1")
    # async def sla(ctx):
    #     await ctx.send('Bd!')
