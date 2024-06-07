"""
Напишите функцию create_user_profile(), которая принимает
 - обязательные аргументы first_name и last_name,
 - а также произвольное количество именованных аргументов для создания профиля пользователя.
Функция должна возвращать словарь, содержащий всю информацию о пользователе.
"""
from pprint import pprint


def create_user_profile():
    pass


pprint(create_user_profile(
    first_name="John",
    last_name="Doe",
    age=30,
    location="New York",
    occupation="Engineer"
))
