from src.faqbot import bot
import asyncio

def configurar():
    @bot.command()
    async def faq(ctx, nome_faq):
        # cur = con_oracle
        # cur.execute(f"select desc from faq where nome = {nome_faq}")
        # desc = cur.fetchall()[0]

        # await ctx.send(desc)
        await asyncio.sleep(1) 
        await ctx.send(nome_faq)
