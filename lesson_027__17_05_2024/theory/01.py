from pprint import pprint


def f(lst: list[int]) -> tuple:
    s = sum(lst)
    l = len(lst)
    pprint(locals())
    return s, l


result = f([1, 2, 3])

print(result)
print(f'Sum {result[0]}')
print(f'Len {result[-1]}')

summa, length = result
print(f'Sum {summa}')
print(f'Len {length}')

pprint(locals())
