from functools import reduce
from typing import Iterator

nums = [1, 2, 3, 4, 5, 6, 7, 8]

""" =========================== map =========================== """
map_object = map(str, nums)
print(map_object)
print(isinstance(map_object, Iterator))
print(*map_object)
print()

map_object_2 = map(lambda x, y: x + y, nums, nums)
print(*map_object_2)
print()

""" =========================== map =========================== """
filter_obj = filter(lambda x: x % 2 == 0, nums)
print(filter_obj)
print(isinstance(filter_obj, Iterator))
print(*filter_obj)
print()

""" =========================== reduce =========================== """
reduce_obj = reduce(lambda x, y: x + y, nums, 10)
print(reduce_obj)
