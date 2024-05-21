"""Написать функцию count_vowels, которая возвращает количество гласных в тексте,
где гласные vowels = 'aeiouy'.

Пример:
text = 'hEllO world'
result = 3
"""


def count_vowels(word: str) -> int:
    vowels = 'aeiouyAEIOUY'

    # ============== variant 1 ====================
    # count = 0
    # for s in word:
    #     if s in vowels:
    #         count += 1
    # return count

    # ============== variant 2 ====================
    return len([s for s in word if s in vowels])


if __name__ == "__main__":
    text = 'hEllO world'
    print(count_vowels(text))
