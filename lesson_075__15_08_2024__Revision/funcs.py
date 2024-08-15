from typing import List


def select_choice(tables: List[str]) -> str:
    if len(tables) == 1:
        return f'SELECT * FROM {tables[0]}'

    elif len(tables) == 2:
        if set(tables) == {'Users', 'Products'}:
            return "SELECT * FROM Users AS u LEFT JOIN Products AS p ON u.id = p.pid"
        elif set(tables) == {'Users', 'Sales'}:
            return 'SELECT * FROM Users AS u LEFT JOIN Sales as s ON u.id = s.sid'
        elif set(tables) == {'Sales', 'Products'}:
            return f"SELECT * FROM Sales AS s LEFT JOIN Products AS p ON s.pid = p.pid"

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
        names = [f'{table}.{f[0]}' for f in fields]
        print(*names, sep='\n')














