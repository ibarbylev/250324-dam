class MyClass:
    pass


class MySubClass(MyClass):
    pass


my_object = MyClass()
my_sub_object = MySubClass()

print(isinstance(my_object, MyClass))        # True
print(isinstance(my_sub_object, MyClass))    # True
print(isinstance(my_object, MySubClass))     # False

"""__mro__ - Method Resolution Order (порядок разрешения методов). 
Он используется для определения порядка, в котором 
классы наследуются и методы/атрибуты ищутся в иерархии классов.
"""
print(MyClass.__mro__)
print(my_object.__class__.__mro__)
# (<class '__main__.MyClass'>, <class 'object'>)
print(MySubClass.__mro__)
# (<class '__main__.MySubClass'>, <class '__main__.MyClass'>, <class 'object'>)