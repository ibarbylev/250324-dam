"""Функции map() и filter() могут быть легко заменены на
list или tuple compression
"""

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert numbers to strings using list compression
print([str(n) for n in nums])

# Get only even items using list compression
print([n for n in nums if n % 2 == 0])

# Get only odd items using generator expression (tuple compression)
print(*(n for n in nums if n % 2 != 0))
