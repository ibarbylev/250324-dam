class MyClass:
    pass


class MySubClass(MyClass):
    pass


my_object = MyClass()
my_sub_object = MySubClass()

print(isinstance(my_object, MyClass))          # True
print(isinstance(my_sub_object, MyClass))      # True
print(isinstance(my_sub_object, MySubClass))   # True
print(isinstance(my_object, MySubClass))       # False

"""__mro__ - Method Resolution Order (порядок разрешения методов). 
Он используется для определения порядка, в котором 
классы наследуются и методы/атрибуты ищутся в иерархии классов.
"""
print(MyClass.__mro__)
print(my_object.__class__.__mro__)
# (<class '__main__.MyClass'>, <class 'object'>)
print(MySubClass.__mro__)
# (<class '__main__.MySubClass'>, <class '__main__.MyClass'>, <class 'object'>)
print(dir(MySubClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
