"""Есть магазин по продаже мороженого. Одна порция стоит 5 евро.
В кассе на момент открытия магазина - 0 евро.
В магазин выстраивается очередь покупателей, у которых есть одна купюра, чтобы оплатить порцию мороженого.

Задача: зная купюры всех покупателей в очереди (конечного размера), понять, получится ли продать мороженое всем
(для этого надо иметь достаточно купюр, чтобы давать сдачу), или не получится.

Существуют купюры следующего номинала: 5, 10, 20, 50 евро.
Напишите функцию, которая принимает список с купюрами покупателей.
Например, если очередь имеет купюры [5, 10, 5, 20], то функция вернет true
(первому покупателю продадут мороженое за 5,
со второго возьмут 10 и дадут сдачу 5,
третьему дадут мороженое за 5,
с четвертого возьмут 20 евро и дадут сдачу 15 купюрами 10 и 5 которые есть в кассе).

Подсказка: кассу можно представить в виде списка, отсортированного по возрастанию.
Когда нужно понять, можно ли дать сдачу, то мы перебираем список кассы и суммируем банкноты в нём.
Если они могут в сумме дать сдачу, то мы их убираем из списка, добавляем банкноту,
которой платили, пересортировываем, и так далее).
"""


def can_sell_icecream(customers: list[int]) -> bool:
    cash_box = []
    customers.sort()

    for customer in customers:
        change_needed = customer - 5  # сумма сдачи, которую надо вернуть покупателю

        # необходимо выдать покупателю сдачу из нашей кассы cash_box
        # начиная с самых крупных банкнот
        # если сдачи не хватает - возвращаем False
        while True:
            for banknote in cash_box:
                if banknote <= change_needed:
                    change_needed -= banknote
                    cash_box.remove(banknote)
                    break
            else:
                break

        if change_needed > 0:
            return False

        # добавляем купюру customer в кассу cash_box и сортируем кассу по убыванию
        cash_box.append(customer)
        cash_box.sort(reverse=True)

    return True


print(can_sell_icecream([5, 10, 10]))   # False
print(can_sell_icecream([5, 5, 10, 10]))  # True
print(can_sell_icecream([5, 10, 5, 20]))  # True
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5]))  # False
print(can_sell_icecream([50, 10, 5, 20, 10, 10, 5, 5, 5, 5]))  # True

