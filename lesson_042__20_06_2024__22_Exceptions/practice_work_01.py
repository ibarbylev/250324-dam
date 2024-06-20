"""Напишите программу, которая будет считывать данные из файла names.txt
и будет формировать список кортежей из пяти полей:
    фамилия, имя, год рождения, курс и баллы.
Обработайте следующие ошибки:
    файла не существует,
    нельзя считать из файла,
    число элементов в стоке на равно 5!
    год рождения, курс и/или баллы не являются числом,
    курс не является числом,
    баллы не являются числом и т.п.
Пример входного файла:
Ivanov		Ivan		1980		2	80
Smith		Ann		    2000		1	67
Petrov		Petro		1999		1	90	43
Schmidt	    Marta		1976		3
Johnson	    John		1965g		5	99
Archer		Lenard		1978		v5	51
"""


class IncorrectAmountOfData(Exception):
    pass


try:
    with open('names.txt', encoding='utf-8') as file:
        for line in file:
            if len(line.split()) != 5:
                pass
                # IncorrectAmountOfData('Число элементов в стоке на равно 5!')
            else:
                surname, name, birth_year, course, points = line.split()
                # искусственно вызываем возможную ошибку
                _, _, _ = int(birth_year), int(course), int(points)
                print(line)


except Exception as e:
    print(f'{e.__class__.__name__} {e}')

