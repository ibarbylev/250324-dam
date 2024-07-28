class Display:
    def __init__(self, temp):
        self.__temp = temp

    @property
    def temperature(self):
        return self.__temp

    @temperature.setter
    def temperature(self, value):
        if 10 < value < 30:
            self.__temp = value
        else:
            raise ValueError(f'Incorrect temperature value {value}!')


m = Display('25')
print(m.temp)  # 25
m.temp = 29
print(m.temp)

try:
    m.temp = 30
except ValueError as e:
    print(e)  # Incorrect temperature value 30!

