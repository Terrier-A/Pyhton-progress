from random import randint

data = []

for i in range(10):
    data.append(randint(0, 99))

print(data)

data2 = [value % 2 for value in data if value >= 50]

print(data2)
