from src.ora import cur
import re

def validar(palavras_chave):
    try: 
        palavras_chave = int(palavras_chave)   
    except:
        if ((not palavras_chave.isspace()) or (len(palavras_chave) > 0)):
            return 1     
    else:
        return 0


def separar_palavras_chave(palavras_chave):
    palavras_chave = palavras_chave.replace(',', ' ').split()
    palavras_chave = '}% and %{'.join(palavras_chave)
    palavras_chave_separadas = '%{' + palavras_chave + '}%'
    
    return palavras_chave_separadas


def juntar_palavras_chave(busca):
    busca = re.sub('}% and %{', ', ', busca)
    busca = busca[2:-2]

    return busca


def selecionar_faq(palavras_chave_separadas):
    try:
        query = f"""with aux as (
    select titulo, descricao, cd_faq from faq where cd_faq = (
        SELECT CD_FAQ FROM (
                            SELECT CD_FAQ, CONTAINS(XML_FAQ, '{palavras_chave_separadas}') score
                            FROM V_XML_FAQ
                            WHERE CONTAINS(XML_FAQ, '{palavras_chave_separadas}') > 0
                            order by score desc
                        )
        FETCH FIRST 1 ROW ONLY)
                )
                
    SELECT a.titulo,
           F_EDITA_DESC_FAQ(a.descricao),
           REGEXP_SUBSTR(F_EDITA_DESC_FAQ(a.descricao), 'http[s]?://[^ ,]+', 1, LEVEL) AS url,
           LEVEL,
           INSTR(F_EDITA_DESC_FAQ(a.descricao), 'http', 1, LEVEL) posicao_inicio,
           INSTR(F_EDITA_DESC_FAQ(a.descricao), ' ', INSTR(F_EDITA_DESC_FAQ(a.descricao), 'http', 1, LEVEL)) posicao_fim 
    FROM aux a
    CONNECT BY INSTR(F_EDITA_DESC_FAQ(a.descricao), ' ', INSTR(F_EDITA_DESC_FAQ(a.descricao), 'http', 1, LEVEL)) > 0 """
        
        cur.execute(query)
        return cur.fetchall()
    
    except:
        return None
     
   
def formatar_faq(faq_selecionado):
    return f"""
{faq_selecionado[0][0]}\n
{faq_selecionado[0][1]}"""
