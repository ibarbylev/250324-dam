"""Дан список именованных тюплов.
Необходимо распечатать каждую строку в формате:
Country: France, Capital: Paris, Population: 67 mln
"""

from collections import namedtuple

Country = namedtuple('Country', ['name', 'capital', 'population'])

country1 = Country(name='France', capital='Paris', population=67000000)
country2 = Country(name='Germany', capital='Berlin', population=83000000)
country3 = Country(name='Italy', capital='Rome', population=59500000)

countries = [country1, country2, country3]


for c in countries:
    print(f"Country: {c.name}, Capital: {c.capital}, Population: {int(c.population/1000000)} mln")

# Country: France, Capital: Paris, Population: 67 mln
# Country: Germany, Capital: Berlin, Population: 83 mln
# Country: Italy, Capital: Rome, Population: 60 mln


