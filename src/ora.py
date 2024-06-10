import oracledb, os

senha = os.environ['SENHA_ORACLE']
connection = oracledb.connect(user ='WNS', password = senha, dsn = '192.168.30.200/ORCL', port = 1521)

cur = connection.cursor()
