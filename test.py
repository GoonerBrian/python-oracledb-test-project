import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER_NAME = os.getenv('DB_USER_NAME')
TABLE_NAME = os.getenv('TABLE_NAME')
p_dns = "//oracle.cise.ufl.edu/orcl"
p_port = "1521"

query_str = f'select * from "{DB_USER_NAME}"."{TABLE_NAME}"'

con = oracledb.connect(
    user=USER_NAME, password=DB_PASSWORD, dsn=p_dns, port=p_port)

print(con.is_healthy())
print(con.thin)
print(con.version)

cur = con.cursor()
cur.execute(query_str)

for row in cur:
    print(row)

cur.close()
con.close()
