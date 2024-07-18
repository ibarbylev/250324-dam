"""Создайте класс BankAccount для представления банковского счета.
Класс должен иметь атрибуты
    - account_number (номер счёта)
    - и balance (баланс),
а также методы
    - deposit() для внесения денег на счёт
    - и withdraw() для снятия денег со счёта.
Затем создайте экземпляр класса BankAccount,
внесите на счёт некоторую сумму и снимите часть денег.
Выведите оставшийся баланс.
Не забудьте предусмотреть вариант, при котором
при снятии баланс может стать меньше нуля.
В этом случае уходить в минус не будем,
вместо чего будем возвращать сообщение "Недостаточно средств на счете".
"""


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Внесение денег на счет."""
        if amount > 0:
            self.balance += amount
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        """Снятие денег со счёта."""
        if amount > self.balance:
            return "Недостаточно средств на счете"
        elif amount > 0:
            self.balance -= amount
            return f"Снято {amount}. Остаток на счете: {self.balance}"
        else:
            return "Сумма снятия должна быть положительной"

    def __str__(self):
        return (f"BankAccount(account_number={self.account_number}, "
                f"balance={self.balance})")

    def __repr__(self):
        return f"BankAccount({self.account_number}{self.balance})"


account = BankAccount("GM00001210121")

account.deposit(1000)
print(f"Баланс после внесения: {account.balance}")
print(account.withdraw(500))
print(f"Баланс после снятия: {account.balance}")
print(account.withdraw(600))
print(f"Баланс после попытки снятия: {account.balance}")
print(account.withdraw(-100))
print(f"Баланс после попытки снятия: {account.balance}")

# Баланс после внесения: 1000
# Снято 500. Остаток на счете: 500
# Баланс после снятия: 500
# Недостаточно средств на счете
# Баланс после попытки снятия: 500
# Сумма снятия должна быть положительной
# Баланс после попытки снятия: 500
