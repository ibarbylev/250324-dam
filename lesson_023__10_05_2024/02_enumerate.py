fruits = ["apple", "potato", "pinapple"]

for index in range(len(fruits)):
    print(index, fruits[index])

print("================================")

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("================================")

print(list(enumerate(fruits)))
