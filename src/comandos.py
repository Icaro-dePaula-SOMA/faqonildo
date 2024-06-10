from src.faqbot import bot
from src.funcoes import validar, separar_palavras_chave, selecionar_faq, formatar_faq, juntar_palavras_chave
import discord, asyncio

def configurar():       
    @bot.event
    async def on_ready():
        await bot.tree.sync()

    @bot.tree.command(description="Procure por um FAQ")
    async def faq(interact:discord.Interaction, palavras_chave:str):
        try:
            await asyncio.sleep(1)
            if(validar(palavras_chave)):
                palavras_chave_separadas = separar_palavras_chave(palavras_chave)

                faq = selecionar_faq(palavras_chave_separadas)

                if faq == None:
                    msg_sem_faq = f"""\nNão encontrei nenhum FAQ contendo "{juntar_palavras_chave(palavras_chave_separadas)}" :thinking: Tenta denovo por favor."""
                    await interact.response.send_message(msg_sem_faq)

                prefixo = f'{interact.user.name}, encontrei um FAQ que pode te ajudar :smiley: \n'         
                resposta = prefixo + formatar_faq(faq) 

                await interact.response.send_message(resposta[0:1800])

                for i in range(1800, len(resposta), 1800):
                    fragmento = resposta[i:i + 1800]
                    await interact.followup.send(fragmento)
            
            await interact.response.send_message('Não consigo procurar por números :confused: tenta digitar algum texto.')

        except:
            if not interact.response.is_done():
                await interact.response.send_message('Tive alguns problemas com as palavras chave, tenta denovo por favor :grimacing:')
                