from src.faqbot import bot
from src.ora import cur
import asyncio

def configurar():
    @bot.command()
    async def faq(ctx, nome_faq):

        query = f"select descricao_old from faq where TITULO = '{nome_faq}'"

        cur.execute(query)

        await asyncio.sleep(1) 

        try:
            query = cur.fetchall()[0][0]
        except:
            await ctx.send(f"Não encontrei nenhum FAQ chamado {nome_faq}, tem certeza que o nome é esse?")
        else:
            await ctx.send(query)
