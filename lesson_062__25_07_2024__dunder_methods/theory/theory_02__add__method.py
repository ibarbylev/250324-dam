class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Cannot add amounts with different currencies")

    def __str__(self):
        return f"{self.amount} {self.currency}"


m1 = Money(100, "eur")
m2 = Money(230, "eur")
try:
    m3 = m1 + m2
    print(m3)           # 330 eur
    print(m3.__dict__)  # {'amount': 330, 'currency': 'eur'}
except Exception as e:
    print(f'{e.__class__.__name__}("{e}")')
    # ValueError("Cannot add amounts with different currencies")


# 330 eur
# {'amount': 330, 'currency': 'eur'}

# ValueError("Cannot add amounts with different currencies")
