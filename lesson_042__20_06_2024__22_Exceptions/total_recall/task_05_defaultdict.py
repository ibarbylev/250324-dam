from collections import defaultdict

my_dict = defaultdict(int)
print(my_dict)              # defaultdict(<class 'int'>, {})

my_dict["apple"] = 5
print(my_dict)              # defaultdict(<class 'int'>, {'apple': 5})

print(my_dict["banana"])    # 0
# автоматически создаёт нулевое значение с типом данных int при первом обращении к ключу
print(my_dict)              # defaultdict(<class 'int'>, {'apple': 5, 'banana': 0})
