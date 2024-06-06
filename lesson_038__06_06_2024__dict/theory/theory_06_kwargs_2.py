def my_function(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)

    print(kwargs.items())

    for key, _ in kwargs.items():
        kwargs[key] = key

    print(kwargs)


my_function(name="John", age=25, height=182)

