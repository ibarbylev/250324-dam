from pprint import pprint


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car('WV', 'Passat')
# car.info = lambda: print(f"{car.brand} {car.model}")
car.__setattr__('info', lambda: print(f"{car.brand} {car.model}"))

car.info()
# WV Passat

pprint(car.__dir__())