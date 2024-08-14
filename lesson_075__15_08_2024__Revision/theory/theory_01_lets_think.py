"""Объясните, что происходит в этом фрагменте программы.
Перечислите ситуации, когда цикл продолжает выполняться,
а когда завершается:
"""

list_of_tables = ["users", "product", "sales"]
str_of_tables = ', '.join(list_of_tables)
tables = ["empty"]

while not set(tables).issubset(list_of_tables):
    tables = input(f"Введите таблицу или список таблиц из набора {str_of_tables}: ").split()
    if set(tables) == {"users", "product"}:
        print("Эти таблицы не связаны. Сделайте другой выбор")
        tables = ["empty"]
