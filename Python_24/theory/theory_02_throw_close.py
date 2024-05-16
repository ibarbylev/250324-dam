def fibonacci_generator():
    try:
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    except GeneratorExit:
        print("Exception GeneratorExit")
    except Exception as e:
        print(f"Exception as {e}")


gen = fibonacci_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
try:
    gen.throw(ValueError("Example error"))  # Бросаем исключение в генератор
except Exception as e:
    print(e.__class__)

gen = fibonacci_generator()
print(next(gen))  # 0
gen.close()
