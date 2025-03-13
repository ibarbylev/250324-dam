from operator import add, sub, mul, truediv

print(add(5, 3))        # Результат: 8
print(sub(10, 2))       # Результат: 8
print(mul(2, 4))        # Результат: 8
print(truediv(16, 2))   # Результат: 8.0


iter_value = map(lambda x, y: x + y, 'abc', 'cdef')
# iter_value = map(add, 'abc', 'cdef')

for item in iter_value:
    print(item)
# ac
# bd
# ce
