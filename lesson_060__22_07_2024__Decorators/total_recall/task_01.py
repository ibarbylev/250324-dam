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

    def make_sound(self):
        pass
        #  ------------------ удалить отсюда --------------------




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

