from src.faqbot import bot
from src.ora import cur
import asyncio


def select(faq_solicitado):
    query = f"select titulo, descricao from faq where titulo = '{faq_solicitado}' or lower(titulo) like '%{str(faq_solicitado).lower()}%'"
    cur.execute(query)
    return cur.fetchall()


def configurar():
    @bot.command()
    async def faq(ctx, faq_solicitado):

        query = select(faq_solicitado)
        await asyncio.sleep(1) 

        tam_query = len(query)

        match tam_query:
            case 0:
                await ctx.send(f'Não encontrei nenhum FAQ chamado "{faq_solicitado}", tem certeza que o nome é esse?\n')

            case 1:
                await ctx.send(f"""
{query[0][0]}\n
{query[0][1]}
### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n""")
            
        if(tam_query > 1):

            lista = ['']
            
            for faq in range(0, 19):
                lista[0] += ((query[faq][0]) + '\n')
            
            await ctx.send(f"""
Não encontrei o FAQ desejado, mas aqui vão alguns possíveis FAQ's para te ajudar:\n
```{lista[0]}```""")

