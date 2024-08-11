"""Используя библиотеку BeautifulSoup 4 , найдите и выведите все ссылки
 (список значений атрибута href всех тегов ссылок <a> из меню навигации
 (<nav> элемент)  в предоставленном HTML-файле <navbar_links.html>

 Ссылки могут быть как в основном меню, так и в выпадающем подменю.

ВАЖНО: Обратите внимание, что в выборку ссылок не должны попадать:
    1. Ссылки, которые находятся вне меню навигации.
        Wrong link1 - Wrong link5
    2. Ссылки, указывающие на элементы с id внутри той же страницы
        Wrong link1
"""

from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    with open(filename, encoding='utf-8') as f:
        return f.read()


html_content = get_html('example_table.html')
soup = BeautifulSoup(html_content, 'html.parser')

table = ...





# AUD Австралийский доллар 58,0043
# AZN Азербайджанский манат 51,7600
# AMD Армянских драмов 22,6655
# BYN Белорусский рубль 28,1601
# BGN Болгарский лев 49,1738

# Курс USD / EUR = 0.9244371976920589
