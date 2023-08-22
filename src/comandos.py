from src.faqbot import bot
from src.ora import cur
import asyncio

def configurar():
    @bot.command()
    async def faq(ctx, nome_faq):
        cur.execute(f"select descricao from faq where TITULO = {nome_faq}")

        query = cur.fetchall()[0][0]

        await asyncio.sleep(1) 
        await ctx.send(nome_faq)
