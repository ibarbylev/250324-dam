from local_settings import dbconfig
from mysql_manager import MySQLConnection


with MySQLConnection(dbconfig) as db:
    db.cursor.execute('SELECT * FROM Users;')

    table_name = "User"
    rows = db.cursor.fetchall()

    print(f" ===== Table {table_name}: =====")
    for row in rows:
        print(row)