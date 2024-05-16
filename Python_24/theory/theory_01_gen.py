def my_generator():
    yield 1
    yield 2
    yield 3


for item in my_generator():
    print(item)

print(' ===================================== ')
g = my_generator()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
