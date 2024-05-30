"""Предположим, у нас есть сложная функция, рассчитывающая стоимость продукта
в зависимости от ставки налога.

    def get_total_cost(price, tax_rate):
        return price * (1 + tax_rate)

Необходимо создать на её основе 3 новые функции,
с фиксированными налоговыми ставками 0%, 9% и 20%:

    get_total_cost_tax_rate_0(price)
    get_total_cost_tax_rate_9(price)
    get_total_cost_tax_rate_20(price)
"""
from functools import partial


def get_total_cost(price, tax_rate):
    return price * (1 + tax_rate)


get_total_cost_tax_rate_0 = partial(get_total_cost, tax_rate=0)
get_total_cost_tax_rate_9 = partial(get_total_cost, tax_rate=0.09)
get_total_cost_tax_rate_20 = partial(get_total_cost, tax_rate=0.20)


print(type(get_total_cost_tax_rate_20))
print(get_total_cost_tax_rate_20(100))
