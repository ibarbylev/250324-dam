class MyClass:
    count = 0

    @classmethod
    def increase_counter_by_1(cls):
        cls.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)


print(MyClass.count)  # 0
MyClass.print_count()  # 0
MyClass.increase_counter_by_1()
MyClass.print_count()  # 1
MyClass.increase_counter_by_1()
MyClass.increase_counter_by_1()
MyClass.increase_counter_by_1()
MyClass.print_count()  # 4



# ===========================
from datetime import date, datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, birth_date_str):
        """birth_date_str = yyyy-mm-dd"""
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()
        age = (today.year - birth_date.year -
               ((today.month, today.day) < (birth_date.month, birth_date.day)))

        return cls(name, age)


person = Person.create_person("John Doe", "1990-07-26")
print(f"{person.name} is {person.age} years old.")  # Вывод: John Doe is 33 years old.
