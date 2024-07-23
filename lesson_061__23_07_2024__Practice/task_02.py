"""
Импортировать классы фигур из предыдущего файла.

Составить список, содержащий по 2 экземпляра каждого класса фигуры.
Вывести на печать площадь каждого объекта в формате:
Area of Circle(name=circle, radius=5): 78.54
с точностью до 2-го знака после запятой
"""
from task_01 import Circle, Square, Rectangle


figures = [
    Circle(name="circle", radius=5),
    Circle(name="circle", radius=3),
    Square(name="square", side=4),
    Square(name="square", side=6),
    Rectangle(name="rectangle", side1=3, side2=4),
    Rectangle(name="rectangle", side1=5, side2=6)
]

for figure in figures:
    area = figure.calculate_area()
    print(f"Area of {figure}: {area:.2f}")


# Area of Circle(name=circle, radius=5): 78.54
# Area of Circle(name=circle, radius=3): 28.27
# Area of Square(name=square, side=4): 16.00
# Area of Square(name=square, side=6): 36.00
# Area of Rectangle(name=rectangle, side1=3, side2=4): 12.00
# Area of Rectangle(name=rectangle, side1=5, side2=6): 30.00
