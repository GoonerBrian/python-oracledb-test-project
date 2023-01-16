import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
p_dns = "//oracle.cise.ufl.edu/orcl"
p_port = "1521"

con = oracledb.connect(
    user=USER_NAME, password=DB_PASSWORD, dsn=p_dns, port=p_port)

print(con.is_healthy())
print(con.thin)
print(con.version)

cur = con.cursor()
cur.execute('select * from "BRIAN.HOBLIN"."CUSTOMERS"')

for row in cur:
    print(row)

cur.close()
con.close()
