def infinity_counter():
    yield 1
    yield 2
    yield 3


N_MAX = 10

int_count = infinity_counter()
for i in range(N_MAX):
    print(next(int_count))
