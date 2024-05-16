from bisect import bisect_left, bisect_right


def grade_right(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect_right(breakpoints, score)
    return grades[i]


def grade_left(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect_left(breakpoints, score)
    return grades[i]


print([grade_right(score) for score in [33, 99, 77, 70, 89, 90, 100]])
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
print([grade_left(score) for score in [33, 99, 77, 70, 89, 90, 100]])
# ['F', 'A', 'C', 'D', 'B', 'B', 'A']
