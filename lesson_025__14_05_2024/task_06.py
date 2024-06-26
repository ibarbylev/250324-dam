"""Создайте текстовый файл persons.txt, где 5 строчек, в каждой фамилия;имя;возраст.
То есть каждая строка - информация о человеке и данные разделены точкой с запятой.
Напишите программу, которая вычитывает данные из файла и печатает их на экран в формате:
Имя: <имя>, Фамилия <фамилия>, Возраст <возраст>.
"""

with open("persons.txt", "r") as file:
    for line in file:
        data = line.strip().split(";")
        surname, name, age = data
        print("Фамилия: {}, Имя: {}, Возраст: {}".format(surname, name, age))
