"""Представьте, что у вас есть класс Coffee с атрибутами
    - цена и
    - название.

Декорировать этот класс по аналогии с предыдущей задачей,
чтобы можно было получить кофе с молоком (стоит дороже),
кофе с сахаром (цена остаётся такой же), двойной кофе (цена удваивается).
"""


class Coffee:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def __str__(self):
        return f"{self.name} (price: {self.price} euro)"


class WithSugar:
    def __call__(self, cls):
        class CoffeeWithSugar(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.name += " with sugar"
                # Цена не изменяется
        return CoffeeWithSugar


class WithMilk:
    def __call__(self, cls):
        class CoffeeWithMilk(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.name += " with milk"
                self.price += 2  # Увеличиваем цену на 2 euro.
        return CoffeeWithMilk


class DoubleCoffee:
    def __call__(self, cls):
        class DoubleCoffee(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.name = "Double " + self.name
                self.price *= 2  # Удваиваем цену
        return DoubleCoffee


@DoubleCoffee()
class DoubleCoffeeCup(Coffee):
    pass


@WithSugar()
class CoffeeWithSugar(Coffee):
    pass


@WithMilk()
class CoffeeWithMilk(Coffee):
    pass


@WithSugar()
@WithMilk()
class CoffeeWithSugarAndMilk(Coffee):
    pass


@DoubleCoffee()
@WithMilk()
class DoubleCoffeeWithMilk(Coffee):
    pass


# Coffee
coffee = Coffee(3, "Coffee")
print(coffee)
# Coffee (price: 3 euro)

# Coffee with suger
coffee_with_sugar = CoffeeWithSugar(3, "Coffee")
print(coffee_with_sugar)
# Coffee with sugar (price: 3 euro)

# Coffee with mill
coffee_with_milk = CoffeeWithMilk(3, "Coffee")
print(coffee_with_milk)
# Coffee with milk (price: 5 euro)

# Coffee with suger and milk
coffee_with_sugar_and_milk = CoffeeWithSugarAndMilk(3, "Coffee")
print(coffee_with_sugar_and_milk)
# Coffee with milk with sugar (price: 5 euro)

# Double coffee
double_coffee_cup = DoubleCoffeeCup(3, "Coffee")
print(double_coffee_cup)
# Double Coffee (price: 6 euro)

# Double coffee with milk
double_coffee_with_milk = DoubleCoffeeWithMilk(3, "Coffee")
print(double_coffee_with_milk)
# Double Coffee with milk (price: 10 euro)





