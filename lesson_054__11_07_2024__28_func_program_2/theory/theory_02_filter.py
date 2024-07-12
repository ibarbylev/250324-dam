from typing import Iterator

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get only even items
filer_iter = filter(lambda x: x % 2 == 0, nums)
print(filer_iter)  # <filter object at 0x7f7edb9de560>
print(list(filer_iter))
print(isinstance(filer_iter, Iterator))

# [0, 2, 4, 6, 8]
