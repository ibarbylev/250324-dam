from typing import Iterator

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert int to string
map_iter = map(str, nums)
print(map_iter)  # <map object at 0x7f7edb9de560>
print(isinstance(map_iter, Iterator))
print(type(map_iter))
print(list(map_iter))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


map_iter = map(lambda x, y: (x + y), nums, nums)
print(map_iter)  # <map object at 0x7f7edb9de560>
print(list(map_iter))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
