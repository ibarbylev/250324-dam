"""Объясните, что происходит в этом фрагменте кода:"""

from itertools import groupby
from operator import itemgetter
a_dict = {'a': 1, 'c': 1, 'b': 5}

dict((i, dict(v)) for i, v in groupby(a_dict.items(), itemgetter(1)))
# Output: {1: {'a': 1, 'c': 1}, 5: {'b': 5}}
