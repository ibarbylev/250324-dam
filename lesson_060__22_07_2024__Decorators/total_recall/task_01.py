"""Дан класс Animal.
Необходимо реализовать классы Dog, Cat, Bird, которые наследуют класс Animal.
Эти классы издают следующие звуки: "Bark", "Meow", "Tweet"

Необходимо также доработать класс Animal (именно Animal!),
чтобы при выводе на печать соответствующего экземпляра
нового класса-наследника печаталось бы:

Animal Dog with the sound "Bark" is called Sharik
Animal Cat with the sound "Meow" is called Ryzhik
Animal Bird with the sound "Tweet" is called Gosha

А при вызове метода make_sound(), печаталось:


"""


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        return f"""Animal {self.__class__.__name__} with the sound {self.sound} is called {self.name}"""

    def make_sound(self):
        print(f"""Animal {self.name} says "{self.sound}".""")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Bird(Animal):
    pass


dog = Dog('Sharik', "Bark")
print(dog)
dog.make_sound()

cat = Cat('Ryzhik', "Meow")
print(cat)
cat.make_sound()

bird = Bird('Gosha', "Tweet")
print(bird)
bird.make_sound()

# Animal Dog with the sound Bark is called Sharik
# Animal Dog says "Bark".
# Animal Cat with the sound Meow is called Ryzhik
# Animal Cat says "Meow".
# Animal Bird with the sound Tweet is called Gosha
# Animal Bird says "Tweet".

print(Bird.__mro__)
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
print(isinstance(cat, Dog))
print(isinstance(cat, Animal))
