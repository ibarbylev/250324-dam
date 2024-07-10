"""Создайте словарь из списка, где ключом будет индекс элемента, 
а значением - значение этого элемента.
"""

my_list = ['apple', 'banana', 'cherry', 'date']

my_dict = dict(enumerate(my_list))

print(my_dict)
# {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'date'}
