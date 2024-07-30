"""Общая идея
Есть два вида растений (Plant): цветы (Flower) и деревья (Tree).

В течение года растения разных видов растут и увядают по-разному,
в зависимости от времени года:
    Весной деревья и цветы растут на 1/2 сезонного роста
    Летом деревья и цветы растут на 1/2 сезонного роста
    Осенью деревья не растут, а цветы срезают (высота 0)
    Зимой ни деревья ни цветы не растут, но к возрасту деревьев добавляется 1 год

Задача: смоделировать рост дерева и цветка на протяжении заданного количества лет,
печатая статус роста каждого растения в зависимости от времени года.
(для этого
    - создаются 2 (или более) объекта дерево (tree) и цветок (flower)
    - далее они объединяются в список plants,
    - в цикле по годам к каждому объекту plants применяется grow_per_season(),
          который по очереди заставляет "проживать" объект все 4 сезона
)

1. Создайте абстрактный класс Plant, которого есть 3 атрибута:
    display_name (читаемое название),
    текущая высота (height),
    текущий возраст (age)
    годовой (сезонный) прирост (delta_grow_per_season)

2. Наследуйте от него два класса Tree и Flower.

    Подумайте, где и как лучше создать метод grow_per_season()?
    (абстрактный метод в Plant и затем его переопределение
    в классах Tree и Flower или универсальный метод в Plant?)

И есть ли смысл сделать какие-либо атрибуты защищёнными (приватными)?
Информация для размышления: стартовый возраст можно установить
при создании объекта класса растения, его можно посмотреть\напечатать,
но изменить его можно только на единичку по истечению года.

4. У класса Plant есть несколько методов:
    do_spring(),
        увеличивает рост на 1/2 от роста в сезон
        "Tree / Flower grows in summer, height is now 00 cm"
    do_summer(),
        увеличивает рост на 1/2 от роста в сезон
        "Tree / Flower grows in summer, height is now 00 cm"
    do_autumn(),
        рост дерева не изменяется, рост цветка уменьшается до 0
        "Tree does not grow in autumn, height is now 00 cm"
        "Flower is cut in autumn, height is now 0 cm"
    do_winter(),
        К возрасту дерева добавляется год
        "Tree / Flower does not grow in winter, height is now 00 cm"
которые меняют свойства age и height в зависимости
    от типа растения
    и правил роста (см условие) в определенный сезон.

Подумайте, какие методы из do_spring(), do_summer(), do_autumn(),
do_winter() можно реализовать в классе Plant
(подсказка: те, в которые растения растут одинаково).

5. Убедитесь, что растения выросли по определенным в условии правилам:
дерево вытянулось, а высота цветка зависит от последнего времени года
и может быть либо 0 (его срезали) либо имеет высоту flower_grow_per_season

"""
from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, display_name, height, age,  delta_grow_per_season):
        self.display_name = display_name
        self.height = height
        self.age = age
        self.delta_grow_per_season = delta_grow_per_season

    def do_spring(self):
        self.height += self.delta_grow_per_season * 0,5
        return f"{self.__class__.__name__} grows in spring, height is now {self.height} cm"

    def do_summer(self):
        self.height += self.delta_grow_per_season * 0, 5
        return f"{self.__class__.__name__} grows in summer, height is now {self.height} cm"

    @abstractmethod
    def do_autumn(self):
        pass

    @abstractmethod
    def do_winter(self):
        return f"{self.__class__.__name__} does not grow in winter, height is now {self.height} cm"

    def grow_per_season(self):
        self.do_spring()
        self.do_summer()
        self.do_autumn()
        self.do_winter()


class Flower(Plant):
    pass


class Tree(Plant):
    pass


tree = Tree('Pine')
flower = Flower('Violet')

plants = [tree, flower]

years = 3
for year in range(years):
    print(f" ========== Year {year} ========== ")
    for plant in plants:
        print(plant)
        plant.grow_per_season()


#  ========== Year 0 ==========
# Tree Pine age=0 height=0 ==========
# Tree grows in spring, height is now 15 cm
# Tree grows in summer, height is now 30 cm
# Tree does not grow in autumn, height is now 30 cm
# Tree does not grow in winter, height is now 30 cm
# Flower Violet age=0 height=0 ==========
# Flower grows in spring, height is now 15 cm
# Flower grows in summer, height is now 30 cm
# Flower is cut in autumn, height is now 0 cm
# Flower does not grow in winter, height is now 0 cm
#  ========== Year 1 ==========
# Tree Pine age=1 height=30 ==========
# Tree grows in spring, height is now 45 cm
# Tree grows in summer, height is now 60 cm
# Tree does not grow in autumn, height is now 60 cm
# Tree does not grow in winter, height is now 60 cm
# Flower Violet age=0 height=0 ==========
# Flower grows in spring, height is now 15 cm
# Flower grows in summer, height is now 30 cm
# Flower is cut in autumn, height is now 0 cm
# Flower does not grow in winter, height is now 0 cm
#  ========== Year 2 ==========
# Tree Pine age=2 height=60 ==========
# Tree grows in spring, height is now 75 cm
# Tree grows in summer, height is now 90 cm
# Tree does not grow in autumn, height is now 90 cm
# Tree does not grow in winter, height is now 90 cm
# Flower Violet age=0 height=0 ==========
# Flower grows in spring, height is now 15 cm
# Flower grows in summer, height is now 30 cm
# Flower is cut in autumn, height is now 0 cm
# Flower does not grow in winter, height is now 0 cm
