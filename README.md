# FAQonildo v1.0

## Pré-Instalação
### Python
- Python versão: 3.11+
- pip

## Instalação

### Dependências
Execute o comando abaixo no diretório do arquivo requirements.txt
```bash
$ python.exe -m pip install --user -r requirements.txt
```

### Configurações banco de dados
Caso necessário, altere o arquivo oracle.py, adequando o usuário do banco de dados, DNS, porta, ou a variável de ambiente SENHA_ORACLE:
```bash
$ import oracledb, os

$ senha = os.environ['SENHA_ORACLE']
$ connection = oracledb.connect(user ='WNS', password = senha, dsn = '192.168.30.200/ORCL', port = 1521)
  
$ cur = connection.cursor()
```

## Variáveis de ambiente

### SENHA_ORACLE
Contém a senha de conexão ao banco de dados Oracle.

### BOT_FAQ_TOKEN
Contém o token de utilização do bot, gerado no discord developers.

License - [MIT](license.txt)
