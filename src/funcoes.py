from src.ora import cur
import re


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


def tem_faq(faq, busca):
    if(faq == None):
        busca = juntar(busca)

        return f"""\nNão encontrei nenhum FAQ contendo "{busca}". Tenta denovo por favor."""

    return f"""
### {faq[0]}\n
{faq[1]}"""
