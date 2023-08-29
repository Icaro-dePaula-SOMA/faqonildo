from src.faqbot import bot
from src.ora import cur
import asyncio

def configurar():
    @bot.command()
    async def faq(ctx, faq_solicitado):

        query = f"select titulo, descricao_old from faq where TITULO = '{faq_solicitado}' or titulo like '%{faq_solicitado}%'"

        cur.execute(query)

        await asyncio.sleep(1) 

        query = cur.fetchall()
        
        if (not len(query)):
            await ctx.send(f"Não encontrei nenhum FAQ chamado {faq_solicitado}, tem certeza que o nome é esse?")
               
        for faq in range(0, len(query)):
            await ctx.send(f'```\n{query[faq][0]}:\n{query[faq][1]}\n```')

