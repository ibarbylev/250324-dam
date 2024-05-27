lst = [('aa', 3), ('av', 2), ('ab', 1), ('aa', 1)]
# lst = [a, v, b, a]
print(lst)


lst.sort(key=lambda x: x[0][1])
print(lst)


# Аналогичный результат, когда функция определена через def:

def f(x):
    return x[0][1]


lst.sort(key=f)
print(lst)
