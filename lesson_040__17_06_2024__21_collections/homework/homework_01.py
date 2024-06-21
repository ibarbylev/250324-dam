"""Напишите программу, которая
 - подсчитывает количество вхождений каждого слова в тексте
 - и выводит на экран наиболее часто встречающиеся слова.

Для решения задачи используйте класс Counter из модуля collections.

Создайте функцию count_words, которая
 - принимает текст в качестве аргумента
 - и возвращает словарь с количеством вхождений каждого слова.

Выведите наиболее часто встречающиеся слова и их количество.

Пример вывода:
Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
sed: 2
lorem: 1
"""

from collections import Counter


def count_words(text) -> dict:
    words = text.lower().split()
    for i, word in enumerate(words):
        words[i] = "".join([s for s in word if s.isalpha()])

    return Counter(words)


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est"
sorted_tuples = sorted(count_words(text).items(), key=lambda x: -x[1])
for i in sorted_tuples[:2]:
    print(f"{i[0]}: {i[1]}")
