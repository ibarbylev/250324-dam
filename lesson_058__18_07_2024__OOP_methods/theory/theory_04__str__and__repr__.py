"""__str__ предназначен больше для пользователя
   __repr__ - для программиста (чтобы однозначно воссоздать объект по описанию)

   Если нет __str__, то в print() отображается __repr__.
   Если есть оба - _str__

  https://www.digitalocean.com/community/tutorials/python-str-repr-functions
"""


class Cat:
    def __init__(self, name=""):
        if name:
            self.name = name
        else:
            self.name = "Anonymous"

    def __str__(self):
        return f'The cat named {self.name}'

    def __repr__(self):
        return f'Cat(name="{self.name}")'

    def eat(self):
        print(f'A cat named {self.name} is eating.  ест.')


cat = Cat('Ryzhik')
print(cat)
