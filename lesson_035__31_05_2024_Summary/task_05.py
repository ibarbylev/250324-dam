"""Отсортируйте список по двум критериям:
   - по длине слова;
   - по длине слова и количеству гласных слове ('aeiouyAEIOUY').
   - по длине слова и алфавиту.
   """


words = ["apple", "orange", "banana", "grape", "peach", "melon", "berry", "plum", "kiwi"]

print(f"Сортировка по длине слова: ")
print(sorted(words, key=len))
print(['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana'])

print(f"Сортировка по длине слова  по количеству гласных слове ('aeiouyAEIOUY'): ")
print(sorted(words, key=lambda word: (len(word), sum(1 for char in word if char in "aeiouyAEIOUY"))))
print(['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana'])

print(f"Сортировка по длине слова и алфавиту: ")
print(sorted(words, key=lambda word: (len(word), word)))
print(['kiwi', 'plum', 'apple', 'berry', 'grape', 'melon', 'peach', 'banana', 'orange'])


