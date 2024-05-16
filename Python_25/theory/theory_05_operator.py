
from operator import itemgetter

data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]

# sorted_data = sorted(data)
# print(sorted_data)
sorted_data = sorted(data, key=itemgetter('age'))
print(sorted_data)

sorted_data = sorted(data, key=lambda x: x['name'])
print(sorted_data)
