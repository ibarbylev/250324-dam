"""Создайте класс Book с приватными атрибутами (__private)
    author (автор)
    title (название)
Реализуйте доступ к этим атрибутам через геттеры и сеттеры.

Далее необходимо создать класс-метод
    - create_book(title, author), который принимает название книги и её автора
                                  и возвращает экземпляр класса Book.

Не забудьте также реализовать метод __str__
"""


class Book:
    pass


if __name__ == '__main__':
    book1 = Book.create_book("Leo Tolstoy", "War and Peace")
    book2 = Book.create_book("Jane Austen", "Pride and Prejudice")

    print(book1)
    print(book2)

# Book War and Peace by Leo Tolstoy
# Book Pride and Prejudice by Jane Austen
