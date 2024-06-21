"""Напишите программу, которая
 - принимает словарь от пользователя и ключ,
 - и возвращает значение для указанного ключа
        с использованием метода get или setdefault.

 Создайте функцию get_value_from_dict, которая
  - принимает словарь и ключ в качестве аргументов,
  - и возвращает значение для указанного ключа, используя метод get или setdefault
        в зависимости от выбранного варианта. Выведите полученное значение на экран.

Пример словаря:
my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

Пример вывода:
Введите ключ для поиска: banana
Использовать метод get (y/n)? y
Значение для ключа 'banana': 6
"""


def get_value_from_dict(dct, key, is_method_get):
    if is_method_get:
        return dct.get(key)
    return dct.setdefault(key, None)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

value = input("Введите ключ для поиска: ")
if input("Использовать метод get (y/n)? ").lower() == "y":
    is_method_get=True
else:
    is_method_get=False


print(f"Значение для ключа '{value}': {get_value_from_dict(my_dict, value, is_method_get)}")

