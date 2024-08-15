"""Объясните, что происходит в этом фрагменте программы."""


def input_columns(table):
    columns = {"users": ["id", "name", "age"],
               "product": ["pid", "prod", "quantity"],
               "sales": ["sid", "pid", "id"]}
    field = input(f"Выберите одно из полей {columns[table]} "
                  f"этой таблицы или введите * для выбора всех: ").strip()
    if field not in columns[table] and field != "*":
        print("Введено некорректное значение. Будет использовано значение *")
        field = "*"
    return "SELECT " + field + " FROM " + table


print(input_columns("users"))


