"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Дан список с именами таблиц.
Программа должна в цикле сделать запрос к каждой из указанных таблиц.
Если таблица есть в базе - вывести на печать её содержимое.
Если нет - вывести сообщение:"The table {table_name} does not exist!"
"""


import mysql.connector
from local_settings import HOST, USER, PASSWORD, DATABASE

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}


def get_table_data(cursor, table_name) -> None:
    try:
        query = f"SHOW TABLES LIKE '{table_name}'"
        result = ...
        if not result:
            print(f"Тhe table <{table_name}> does not exist!")
            return




        rows = ...

        print(f" ===== Table '{table_name}': =====")
        for row in rows:
            print(row)

    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    pass


    for name in ['Users', 'Products', 'Sales', 'No_name']:
        get_table_data(cursor, name)


#  ===== Table 'Users': =====
# (1, 'John Doe', 30)
#  ===== Table 'Products': =====
# (1, 'Laptop', 20)
#  ===== Table 'Sales': =====
# (1, 1, 1)
# Тhe table <No_name> does not exist!
