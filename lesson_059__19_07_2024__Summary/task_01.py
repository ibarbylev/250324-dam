"""Создать класс животных, имеющий атрибут species,
и далее создать объекты этого класса:
3 вида животных - собака, кошка и лошадь.
(Animal -> dog, cat, horse)
Не забудьте при выводе экземпляра класса на печать отобразить значение его атрибутов.
"""


class Animal:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f'Animal({self.species})'


dog = Animal('dog')
cat = Animal('cat')
horse = Animal('horse')

print(dog)
print(cat)
print(horse)

# Animal(dog)
# Animal(cat)
# Animal(horse)
