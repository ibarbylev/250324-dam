class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Cannot add amounts with different currencies")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        raise ValueError("Cannot subtract amounts with different currencies")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Money(self.amount * factor, self.currency)
        raise TypeError("Factor must be a number")

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            return Money(self.amount / divisor, self.currency)
        raise TypeError("Divisor must be a number")

    def __eq__(self, other):
        if self.currency == other.currency:
            return self.amount == other.amount
        return False

    def __lt__(self, other):
        if self.currency == other.currency:
            return self.amount < other.amount
        raise ValueError("Cannot compare amounts with different currencies")

    def __le__(self, other):
        if self.currency == other.currency:
            return self.amount <= other.amount
        raise ValueError("Cannot compare amounts with different currencies")

    def __gt__(self, other):
        if self.currency == other.currency:
            return self.amount > other.amount
        raise ValueError("Cannot compare amounts with different currencies")

    def __ge__(self, other):
        if self.currency == other.currency:
            return self.amount >= other.amount
        raise ValueError("Cannot compare amounts with different currencies")

    def __str__(self):
        return f"{self.amount} {self.currency}"


# Примеры использования
money1 = Money(50, "USD")
money2 = Money(20, "USD")
money3 = Money(100, "EUR")

print(money1 + money2)  # Вывод: 70 USD
print(money1 - money2)  # Вывод: 30 USD
print(money1 * 2)       # Вывод: 100 USD
print(money1 / 2)       # Вывод: 25 USD

print(money1 == money2)  # Вывод: False
print(money1 > money2)   # Вывод: True
print(money1 < money3)   # Вывод: ValueError: Cannot compare amounts with different currencies
