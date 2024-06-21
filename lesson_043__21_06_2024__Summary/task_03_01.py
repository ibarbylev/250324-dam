"""Попробуйте повторить это решение для обычного, а не упорядоченного словаря.
Если разница в результатах?
"""

dct = {"orange": 2, "apple": 5, "banana": 2}
print(dct)   # OrderedDict({'orange': 2, 'apple': 5, 'banana': 2})

new_dict = dict(
    # Здесь отсутствует одна строка кода:
    sorted(dct.items(), key=lambda x: (-x[1], x[0]))
)
print(new_dict)   # OrderedDict({'apple': 5, 'banana': 2, 'orange': 2})

