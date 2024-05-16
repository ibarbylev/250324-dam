def my_generator():
    received_value = yield 1
    yield received_value + 1


gen = my_generator()
# print(gen.send(None))  # Выводит 1
print(next(gen))      # Выводит 1
print(gen.send(10))   # Выводит 11
