def my_function(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)

    print(kwargs.items())

    for key, value in kwargs.items():
        print(key, value)  # Выводит имена аргументов и их значения


my_function(name="John", age=25, height=182)

