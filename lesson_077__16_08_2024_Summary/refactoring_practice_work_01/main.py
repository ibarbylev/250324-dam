from local_settings import dbconfig
from mysql_manager import MySQLConnection
from query_templates import *


with MySQLConnection(dbconfig) as db:
    db.cursor.execute('SELECT * FROM Users;')

    table_name = "User"
    rows = db.cursor.fetchall()

    # print(f" ===== Table {table_name}: =====")
    # for row in rows:
    #     print(row)

    for name in ['Users', 'Products', 'Sales', 'No_name']:
        print(f" ===== Table {table_name}: =====")
        row = db.simple_select(s_query, name)
        print(row)
