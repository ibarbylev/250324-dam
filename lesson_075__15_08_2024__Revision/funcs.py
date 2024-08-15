from typing import List


def select_choice(tables: List[str]) -> str:
    if len(tables) == 1:
        return f'SELECT * FROM {tables[0]}'

    elif len(tables) == 2:
        if set(tables) == {'Users', 'Products'}:
            return "SELECT * FROM Users AS U LEFT JOIN Products AS P ON U.id = P.pid"
        elif set(tables) == {'Users', 'Sales'}:
            return 'SELECT * FROM Users AS U LEFT JOIN Sales as S ON U.id = S.sid'
        elif set(tables) == {'Sales', 'Products'}:
            return f"SELECT * FROM Sales AS S LEFT JOIN Products AS p ON S.pid = P.pid"

    elif len(tables) == 3:
        return """SELECT 
                U.name, P.prod, P.quantity
            FROM
                Sales AS S
                    LEFT JOIN
                Users AS U ON S.id = U.id
                    LEFT JOIN
                Products AS P ON S.pid = P.pid"""

    else:
        return "Error input!!!!"


def show_fields(cursor, tables: List[str]) -> None:
    for table in tables:
        query = f'DESCRIBE {table};'
        cursor.execute(query)
        fields = cursor.fetchall()
        names = [f'{table[0]}.{f[0]}' for f in fields]
        print(*names, sep='\n')


def get_rows(cursor, tables, field_name, value):
    query = select_choice(tables)
    query += f' WHERE {field_name} = {value};'
    # print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    print(*rows, sep='\n')













