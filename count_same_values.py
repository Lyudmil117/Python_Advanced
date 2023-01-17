values = {}

data = list(map(float, input().split(" ")))
for value in data:
    if value not in values:
        values[value] = 0

    values[value] += 1

for k, v in values.items():
    print(f'{k} - {v} times')
