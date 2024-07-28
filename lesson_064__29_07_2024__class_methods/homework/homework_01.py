"""Реализуйте класс Employee, представляющий сотрудника компании.
Класс должен иметь статическое поле company с названием компании,
    а также методы:
        set_company(cls, name):
                метод класса для изменения названия компании
        __init__(self, name, position):
                конструктор, принимающий имя и должность сотрудника
        get_info(self):
            метод, возвращающий информацию о сотруднике
            в виде строки (имя, должность, название компании)
"""


class Employee:
    company = "My Company"

    @classmethod
    def set_company(cls, name):
        cls.company = name

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return (f"Name: {self.name}, Position: {self.position}, "
                f"Company: {Employee.company}")


emp1 = Employee("Alice", "Software Engineer")
emp2 = Employee("Bob", "Product Manager")

print(emp1.get_info())
print(emp2.get_info())
# Name: Alice, Position: Software Engineer, Company: Default Company
# Name: Bob, Position: Product Manager, Company: Default Company

Employee.set_company("Tech Innovators")

print(emp1.get_info())
print(emp2.get_info())
# Name: Alice, Position: Software Engineer, Company: Tech Innovators
# Name: Bob, Position: Product Manager, Company: Tech Innovators
