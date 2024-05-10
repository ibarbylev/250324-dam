"""Напишите программу, которая открывает текстовый файл с именем input.txt,
считывает его содержимое и записывает в файл с именем output.txt, меняя порядок слов на обратный.
Каждое слово должно быть записано на отдельной строке.
Используйте цикл for и методы readlines(), split() и reverse() для решения задачи.

Пример содержимого файла input.txt:
Hello, World! How are you?

Пример содержимого файла output.txt:
you?
are
How
World!
Hello,
"""

# 0.) create input.txt
# 1.) read input.txt
# 2.) transform text from input.txt
# 3.) write output.txt

text = 'Hello, World! How are you?'
with open("input.txt", "w", encoding="utf-8") as f:
    print(f.write(text))