from operator import add
from itertools import accumulate


result = accumulate([1, 2, 3], add)
print(*result)


result_2 = accumulate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], add)
print(*result_2)
