from collections import namedtuple

# Создаем именованный кортеж с именами полей 'name' и 'age'
Person = namedtuple('Person', ['name', 'age'])

person1 = Person(name='Alice', age=30)
print(person1.name) 
print(person1.age)

person2 = Person('Ivan', 31)
print(person2.name)
print(person2.age)


# Alice
# 30
# Ivan
# 31