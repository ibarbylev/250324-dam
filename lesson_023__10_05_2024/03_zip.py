print(list(zip(('a', 1), ('b', 2), ('c', 3), ('d', 4))))

print(list(zip(('a', 1, 2, 2), ('b', 2, 2), ('c', 3, 2), ('d', 4))))

print(zip(('a', 1, 2, 2), ('b', 2, 2), ('c', 3, 2), ('d', 4)))

for line in zip(('a', 1, 2, 2), ('b', 2, 2), ('c', 3, 2), ('d', 4)):
    print(line)

for line in list(zip(('a', 1, 2, 2), ('b', 2, 2), ('c', 3, 2), ('d', 4))):
    print(line)
