"""Напишите программу, которая считывает 5 чисел с клавиатуры и записывает их в текстовый файл.
"""
# -------- var 1 ---------
# numbers = []
# for i in range(5):
#     num = input("Введите число {}: ".format(i+1))
#     numbers.append(num)
#
# with open("numbers.txt", "w") as file:
#     for num in numbers:
#         file.write(num + "\n")

# -------- var 2 ---------
# numbers = []
# for i in range(5):
#     num = input("Введите число {}: ".format(i+1))
#     numbers.append(num)
#
# with open("numbers.txt", "w") as file:
#     file.write(";".join(numbers))
# print("Числа записаны в столбец в файл numbers.txt")

# -------- var 3 ---------
# numbers = ''
# for _ in range(5):
#     numbers += input("Введите число: ") + "\n"
#
# with open("numbers.txt", "w") as file:
#     file.write(numbers)

# -------- var 4 ---------
# numbers = [input("Введите число: ") for _ in range(5)]
#
# with open("numbers.txt", "w") as file:
#     file.write(", ".join(numbers))

# -------- var 5 ---------
numbers_input = input("Введите 5 чисел, разделенных пробелом: ")
numbers_list = numbers_input.split()

numbers = [int(num) for num in numbers_list]

with open('numbers.txt', 'w') as file:
    for number in numbers:
        # file.write(f"{number}\t")
        file.write(f"{number}")

print(numbers)

print("Числа успешно записаны в файл 'numbers.txt'.")