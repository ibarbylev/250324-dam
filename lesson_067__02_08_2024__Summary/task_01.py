"""Создайте класс Person с атрибутами name и age.
Реализуйте метод __init__ для инициализации этих атрибутов.
Создайте класс метод from_birth_year() для создания экземпляра
класса Person по году рождения (возраст необходимо вычислить автоматически
с помощью пакета datetime)

Выведите информацию о персоне, созданной через этот альтернативный конструктор.
"""
import datetime


def get_age_using_birth_year( birth_year):
    """Функция возвращает возраст в годах по году рождения
    birth_year = 1991
    :return 33
    (УДАЛИТЬ эту функцию после создания класс-метода!)
    """
    current_year = datetime.date.today().year
    age = current_year - birth_year
    return age


class Person:
    pass


person = Person.from_birth_year("Darya", 1991)
print(person)
# Name: Darya, Age: 33 years
