"""Напишите программу, которая принимает список слов от пользователя
и использует генераторное выражение (comprehension) для создания нового списка,
содержащего только те слова, которые начинаются с гласной буквы.
Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.
В результате программа должна вывести новый список, содержащий только слова,
начинающиеся с гласной буквы и записанные в верхнем регистре.

"""


def transform_words(words: list[str]) -> list[str]:
    vowels = 'aeiouyAEIOUY'
    starting_with_vowels = (w for w in words if w[0] in vowels)
    transformed_words = map(str.upper, starting_with_vowels)
    return list(transformed_words)


words = ["apple", "orange", "banana", "umbrella", "ice", "grape", "elephant"]

print(transform_words(words))
# ['APPLE', 'ORANGE', 'UMBRELLA', 'ICE', 'ELEPHANT']
