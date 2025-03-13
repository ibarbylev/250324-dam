# декларация генератора
def gen():
    print('---------')
    yield 1
    print('---------')
    yield 2
    print('---------')
    yield 3
    print('---------')


# initiate generator (инициализация генератора)
g = gen()

try:
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
except StopIteration as e:
    print(f"{e.__class__.__name__}: {e}")


"""Почему сразу нельзя сделать: print(gen().__next__()) ?

Ответ в следующем файле theory
"""
