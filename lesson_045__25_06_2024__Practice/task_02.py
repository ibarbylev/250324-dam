"""В исходных данных есть дата рождения, но правило проверки возраста требует проверку возраста.
Нужно реализовать разницу между текущей датой и датой рождения клиента с целью проверки его возраста.
"""
from datetime import datetime


class AgeException(Exception):
    pass


def age_validation(birth_date: str) -> bool:
    # birth_date = '2005-03-28'
    date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()
    date_plus_18_years = date_obj.replace(year=date_obj.year + 18)
    today = datetime.now().date()

    if today < date_plus_18_years:
        raise AgeException("The client's age cannot be less than 18 years!")
    return True


try:
    print(age_validation('2005-03-28'))  # True
    print(age_validation('2015-03-28'))
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')

# True
# AgeException: The client's age cannot be less than 18 years!
