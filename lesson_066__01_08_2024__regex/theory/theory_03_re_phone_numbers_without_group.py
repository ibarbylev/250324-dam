import re

TEXT = """ 111 22 33-aad 232-15-11 ff 15 
15 555-22-78 223/99-37 223/25/987 123-35 26 258-85-45 
"""

pattern = r'\d{3} \d{2} \d{2}|\d{3}-\d{2}-\d{2}|\d{3}\/\d{2}\/\d{2}'

result = re.findall(pattern, TEXT)
print(result)
# ['111 22 33', '232-15-11', '555-22-78', '223/25/98', '258-85-45']

print(*re.finditer(pattern, TEXT))
result = [match.group(0) for match in re.finditer(pattern, TEXT)]
print(result)
# ['111 22 33', '232-15-11', '555-22-78', '223/25/98', '258-85-45']


""" re.search - если находит совпадение, возвращает полную информацию
Если не находит - возвращает None
"""

match = re.search(pattern, TEXT)
print(match.group())  # 111 22 33

match = re.search(r'asdfasdfasdf', TEXT)
print(match)  # None


