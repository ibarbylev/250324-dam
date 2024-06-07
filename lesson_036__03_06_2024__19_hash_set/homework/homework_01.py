"""Напишите программу, которая принимает список слов
и возвращает список, содержащий только анаграммы.
Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
Создайте функцию anagrams, которая принимает список слов в качестве аргумента
и возвращает список анаграмм.
Используйте множества и сортировку букв в слове для проверки на анаграмму.
Выведите результат на экран.

Пример переданного списка слов:

['cat', 'dog', 'tac', 'god', 'act']
Пример вывода:
Анаграммы: [['dog', 'god'], ['cat', 'tac', 'act']]
"""


def anagrams(words_lst):
    anagrams_list: list[list[str]] = []
    for word in words_lst:
        for anagram_lst in anagrams_list:
            if sorted(anagram_lst[0]) == sorted(word):
                anagram_lst.append(word)
                break
        else:
            # начинаем новый список анаграмм
            anagrams_list.append([word])
    return anagrams_list


words = ['cat', 'dog', 'tac', 'god', 'act']
print(f"Анаграммы: {anagrams(words)}")


