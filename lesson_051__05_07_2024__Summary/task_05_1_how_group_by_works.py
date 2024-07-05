"""This is how groupby works."""

from itertools import groupby
from operator import itemgetter

for k, v in groupby('AAAABBBCCDAABBB', key=None):
    print(k, list(v))

# A ['A', 'A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# D ['D']
# A ['A', 'A']
# B ['B', 'B', 'B']
print(*groupby(groupby('AAAABBBCCDAABBB'), itemgetter(0)))