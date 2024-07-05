"""This is how groupby works."""

from itertools import groupby
from operator import itemgetter

a_dict = {'a': 1, 'c': 1, 'b': 5}

for k, v in groupby(a_dict.items(), itemgetter(1)):
    print(k, list(v))

print(a_dict.items())
# 1 [('a', 1), ('c', 1)]
# 5 [('b', 5)]
