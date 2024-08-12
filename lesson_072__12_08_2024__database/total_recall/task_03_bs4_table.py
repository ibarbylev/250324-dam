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

table = soup.find('table', class_='data')
rows = table.find_all('tr')

usd, eur = 0, 1
for row in rows:
    items = row.find_all('td')
    if len(items) == 5:
        _, code, _, desc, value = items
        print(code.text, desc.text, value.text)
        if 'USD' == code.text:
            usd = float(value.text.replace(',', '.'))
        if 'EUR' == code.text:
            eur = float(value.text.replace(',', '.'))

print(f"\nКурс евро к доллару: {usd / eur:.4f}")


# AUD Австралийский доллар 58,0043
# AZN Азербайджанский манат 51,7600
# AMD Армянских драмов 22,6655
# BYN Белорусский рубль 28,1601
# BGN Болгарский лев 49,1738

# Курс USD / EUR = 0.9244371976920589
