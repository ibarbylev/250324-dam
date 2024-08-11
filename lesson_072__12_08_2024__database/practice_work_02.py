"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Программа должна
 - вывести все имена из таблицы users,
 - дать пользователю выбрать одно из них
 - и вывести все покупки этого пользователя.

 Если покупок по запрашиваемому пользователю не найдено, то выводим:
    "User {user_name} has no purchases"
"""


import mysql.connector
from local_settings import HOST, USER, PASSWORD, DATABASE
from practice_work_01 import get_table_data

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}


if __name__ == "__main__":
    pass

    # Получаем список пользователей
    get_table_data(cursor, ...)

    user_name = input('Please enter the username: ')
    try:

        rows = ...

        if rows:
            print(f" ===== Purchases of User <{user_name}> : =====")
            for row in rows:
                print(row)
        else:
            print(f'User {user_name} has no purchases')

    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


#  ===== Table 'Users': =====
# (1, 'John Doe', 30)
# Please enter the username: John Doe
#  ===== Purchases of User <John Doe> : =====
# ('John Doe', 'Laptop', 20)




