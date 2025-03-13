def infinity_counter():
    n = 1
    while True:
        yield n


N_MAX = 10

int_count = infinity_counter()
for i in range(N_MAX):
    print(next(int_count))
