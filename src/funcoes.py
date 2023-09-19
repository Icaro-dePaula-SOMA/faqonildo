from src.ora import cur
import re


def vazia(busca):
    if busca.isspace() or len(busca) == 0:
        return 1


def separar(busca):
    busca = busca.replace(',', ' ').split()
    busca = '}% and %{'.join(busca)
    busca = '%{' + busca + '}%'

    return busca


def juntar(busca):
    busca = re.sub('}% and %{', ', ', busca)
    busca = busca[2:-2]

    return busca


def select(busca):
    query = f"""
select titulo, descricao from faq where cd_faq = (
    SELECT CD_FAQ FROM (
                        SELECT CD_FAQ, CONTAINS(XML_FAQ, '{busca}') score
                        FROM V_XML_FAQ
                        WHERE CONTAINS(XML_FAQ, '{busca}') > 0
                        order by score desc
                    )
    FETCH FIRST 1 ROW ONLY)"""
    
    cur.execute(query)
    return cur.fetchone()


def corrige(texto):
    try:
        texto = texto.replace('&gt;', '>')
    except:
        pass

    try:
        texto = str(texto).replace('<img src="', '(')
    except:
        pass
    else:
        try:
            texto = texto.replace('.png">', '.png)')
        except:
            texto = texto.replace('.jpg">', '.jpg)')
        else:
            pass
    
    cur.execute(f"select F_EDITA_DESC_FAQ('{texto}') from dual")

    texto = cur.fetchone()[0]

    return texto


def tem_faq(faq, busca):

    if(faq == None):
        busca = juntar(busca)
        return f"""\nNão encontrei nenhum FAQ contendo "{busca}". Tenta denovo por favor."""
    
    desc = corrige(str(faq[1]))

    return f"""
### {faq[0]}\n
{desc}"""
