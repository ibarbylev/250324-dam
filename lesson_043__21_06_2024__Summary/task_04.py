"""Какие 3 символа (включая пробелы и знаки препинания) чаще всего повторяются в этой фразе:
'Coco Chanel: Je ne me soucie pas de ce que vous pensez de moi. Je ne pense pas à vous du tout.'

Примечание: задача уже была решена, но снова кто-то удалил одну строка кода.
Пожалуйста, восстановите эту строку!
"""

from collections import Counter

text = 'Coco Chanel: Je ne me soucie pas de ce que vous pensez de moi. Je ne pense pas à vous du tout.'
# Здесь отсутствует одна строка кода:
char_num = sorted(Counter(text).items(), key=lambda x: -x[1])
print(*char_num[:3], sep="\n")


