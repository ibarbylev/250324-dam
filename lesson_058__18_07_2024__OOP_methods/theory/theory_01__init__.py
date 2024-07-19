class Cat(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'Кот {self.name} ест.')


cat = Cat('Ryzhik')
cat.eat()
print(dir(Cat))
print(cat.__dir__())
