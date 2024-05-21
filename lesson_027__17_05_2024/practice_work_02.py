"""С помощью функции count_vowels необходимо написать функцию list_transform,
которая из списка слов создаёт новый список количества гласных в этих словах.
И выводит полученный список на печать в виде строки, разделённой пробелами.

words = ['apple', 'orange', 'banana']
vowels_in_words = [2, 3, 3]

Функцию count_vowels необходимо импортировать из предыдущего модуля.
"""

from practice_work_01 import count_vowels


def list_transform(words: list[str]) -> None:
    vowels_new = [count_vowels(word) for word in words]

    # ============ variant 1 =====================
    # print(*vowels_new)

    # ============ variant 2 =====================
    print(" ".join([str(i) for i in vowels_new]))


list_transform(['apple', 'orange', 'banana'])

