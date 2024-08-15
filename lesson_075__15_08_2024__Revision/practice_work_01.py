"""В базе данных ich_edit три таблицы.
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Написать мини-интерфейс к базе данных, который умеет выполнять разные команды.
Выбрать таблицу для запроса.

1. Предусмотреть возможность выбрать несколько таблиц.
Вывести результат их соединения, если это возможно, или сообщение об ошибке.

2. Выбрать одно поле из выбранной таблицы и искомое значение этого поля.
Вывести все подходящие строки.
"""

"""================= Домашнее Задание ===================
1. Доработать мини-интерфейс к базе данных, который был сделан на занятии. 
Новые возможности интерфейса:

2. Ввести список полей выбранной таблицы.
При вводе искомого значения добавить возможность выбора знака - 
найти записи, в которых выбранное поле больше, меньше или равно введенному значению.
"""

import mysql.connector
from local_settings import HOST, USER, PASSWORD, DATABASE
from funcs import show_fields, get_rows

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        # 1. Предложить пользователю ввести набор таблиц (1, 2, 3)
        text_help = "Введите комбинацию полей [Users, Products, Sales] (1, 2 или 3) через пробел: "
        tables = ["Users", "Products"]
        # tables = input(text_help).split()

        # 2. Из введённых таблиц выбрать 1 их 7 вариантов запросов.
        # query = select_choice(tables) + ';'

        # 3. Вывести список полей собранной таблицы.
        show_fields(cursor, tables)

        # 4. Принять от пользователя имя поля и его значение.
        text_help_2 = "Введите поле, знак (=|>|<) и значение поля через пробел: "
        field_name, sign, value = input(text_help_2).split()

        # 5. Добавить к запросу из п 2 'WHERE + условие',
        #    - выполнить запрос и
        #    - вывести результат
        get_rows(cursor, tables, field_name, sign, value)

