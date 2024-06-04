set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1.intersection(set2)
union = set1.union(set2)
difference = set1.difference(set2)
symmetric_difference = set1.symmetric_difference(set2)
print(intersection)  # Выводит {2, 3}
print(union)  # Выводит {1, 2, 3, 4}
print(difference)  # Выводит {1}
print(symmetric_difference)  # Выводит {1, 4}

print(set1.intersection(set2) == set1 & set2)  # True
print(set1.union(set2) == set1 | set2)    # True
print(set1.difference(set2) == set1 - set2)    # True
print(set2.difference(set1) == set2 - set1)    # True
print(set1.symmetric_difference(set2) == set1 ^ set2)    # True
