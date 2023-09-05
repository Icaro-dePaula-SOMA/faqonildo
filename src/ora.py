import oracledb


connection = oracledb.connect(user ='WNS', password = 'AD03AR02', dsn = '192.168.30.200/ORCL', port = 1521)

cur = connection.cursor()
