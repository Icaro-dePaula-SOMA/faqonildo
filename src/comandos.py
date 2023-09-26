from src.faqbot import bot
from src.funcoes import vazia, separar, select, tem_faq
import asyncio


def configurar():   
    @bot.command()
    async def faq(ctx, busca = ''):
        await asyncio.sleep(1)

        if(not vazia(busca)):
            busca = separar(busca)

            faq = select(busca)

            resposta = tem_faq(faq, busca) 

            for i in range(0, len(resposta), 1800):
                parte = resposta[i:i + 1800]
                await ctx.send(parte)
            return      

        await ctx.send('Sua pesquisa está vazia, tenta denovo por favor.')


    @bot.slash_command(name='busca', description='Procure por um FAQ', )
    async def busca(ctx, faqe):
        await asyncio.sleep(1)

        if(not vazia(faqe)):
            busca = separar(faqe)

            faqe = select(busca)

            resposta = tem_faq(faqe, busca) 

            for i in range(0, len(resposta), 1800):
                parte = resposta[i:i + 1800]
                await ctx.respond(parte)
            return
        
        await ctx.respond('Sua pesquisa está vazia, tenta denovo por favor.')
        

    # @bot.slash_command(name='ja_pode', description='Já pode almoçar?', )
    # async def busca(ctx):
    #     await asyncio.sleep(1)

    #     await ctx.respond('Ainda nn')