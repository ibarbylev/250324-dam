def sub_generator():
    yield 'Sub generator'
    yield 'Completed sub generator'


def main_generator():
    yield 'Main generator'
    yield from sub_generator()
    yield 'Completed main generator'


gen = main_generator()
for item in gen:
    print(item)
