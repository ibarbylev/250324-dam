"""Создать абстрактный класс Fountain
с абстрактным методом pour_water().

На его основе создать классы:
    MusicalFountain с методом play_music(),
    LightFountain с методом shine_light(),
    и LightAndMusicalFountain с методами play_music() и shine_light().
    (каждый из этих методов возвращает соответствующую строку -
    см. вывод в конце файла)

Подумайте, какого типа методы могут быть у этих классов?
(classmethod, staticmethod или обычный)
"""


class Fountain:
    pass


class MusicalFountain:
    pass


class LightFountain(Fountain):
    pass


class LightAndMusicalFountain(Fountain):
    pass



musical_fountain = MusicalFountain()
print(musical_fountain.pour_water())
print(musical_fountain.play_music())

light_fountain = LightFountain()
print(light_fountain.pour_water())
print(light_fountain.shine_light())

light_and_musical_fountain = LightAndMusicalFountain()
print(light_and_musical_fountain.pour_water())
print(light_and_musical_fountain.play_music())
print(light_and_musical_fountain.shine_light())

# Water is pouring from the Musical Fountain.
# The Musical Fountain is playing music.
# Water is pouring from the Light Fountain.
# The Light Fountain is shining light.
# Water is pouring from the Light and Musical Fountain.
# The Light and Musical Fountain is playing music.
# The Light and Musical Fountain is shining light.
