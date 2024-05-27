"""Считать данные из файла students.txt, где записаны разделенные запятыми:
 фамилия, имя, год рождения, курс, средний балл.

Перед началом работы необходимо будет создать файл students.txt из списка students.

students = [
    ["John", "Doe", 2003, "Engineering", 88],
    ["Jane", "Smith", 2002, "Mathematics", 88],
    ["Dave", "Jones", 2004, "Engineering", 81],
    ["Eve", "Williams", 2003, "Mathematics", 81],
    ["Alice", "Brown", 2004, "Physics", 81]
]

Реализовать функцию, которая будет выводить на экран строки, отсортированные по 2-м полям:
 - средний балл и
 - курс.
Отформатировать вывод по максимальному значению в каждом поле с выравниванием каждого значения по правому краю.
Значения полей должны разделять как минимум одним пробелом.
"""


def get_data_from_file(filename: str) -> list[list[str]]:
    students = []

    ...

    return students


def get_widths(matrix: list[list[str]]) -> list[int]:
    columns: int = len(matrix[0])
    widths = []

    for col in range(columns):
        max_width = max([len(row[col]) for row in matrix])
        widths.append(max_width)

    return widths


def get_sort_info_by_2_cols(matrix: list[list[str]], col_1, col_2) -> None:
    """Сортировка матрицы по двум столбцам: col_1 и col_2"""

    matrix.sort(key=lambda x: ...)

    w = get_widths(matrix)

    for line in matrix:
        print(" ".join([f"{line[i]:{w[i]}}" for i in range(len(line))]))


students = get_data_from_file('students.txt')
get_sort_info_by_2_cols(students, -1, -2)
