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
    with mysql.connector.connect(**dbconfig) as connection:
        with connection.cursor() as cursor:

            try:
                # Получаем список пользователей
                get_table_data(cursor, 'Users')

                user_name = input('Please enter the username: ')

                cursor.execute(f"""
                    SELECT 
                        U.name, P.prod, P.quantity
                    FROM
                        Sales AS S
                            LEFT JOIN
                        Users AS U ON S.id = U.id
                            LEFT JOIN
                        Products AS P ON S.pid = P.pid
                    WHERE
                        U.name = '{user_name}';
                """)

                rows = cursor.fetchall()

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




