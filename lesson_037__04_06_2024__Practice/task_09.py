"""Напишите функцию, которая получает на вход
    две строки с перечислением интересов и хобби двух пользователей, и
    вычисляет процент совпадения.

Процент рассчитывается, как отношение числа совпадений к максимальному числу интересов
одного из участников.

Использовать множества.
"""


def match_percentage(interests_1: str, interests_2: str) -> float:
    interests1 = set(interests_1.split(", "))
    interests2 = set(interests_2.split(", "))

    common_interests = interests1 & interests2
    max_interests = max(len(interests1), len(interests2))

    return (len(common_interests) / max_interests) * 100


user1_interests = "путешествия, фотография, кино, музыка"
user2_interests = "фотография, кино, литература, спорт"

result = match_percentage(user1_interests, user2_interests)
print(f"Процент совпадения интересов: {result:.2f} %")
