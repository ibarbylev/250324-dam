"""Отсортируйте список по двум критериям:
   - по алфавиту;
   - по количеству гласных слове ('aeiouyAEIOUY').
   """


words = ["apple", "orange", "banana", "grape", "peach", "melon", "berry", "plum", "kiwi"]

print(f"Сортировка по длине слова: ")
print(sorted(words, key=...))
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']

print(f"Сортировка по длине слова и алфавиту: ")
print(sorted(words, key=...))
# ['kiwi', 'plum', 'apple', 'berry', 'grape', 'melon', 'peach', 'banana', 'orange']


