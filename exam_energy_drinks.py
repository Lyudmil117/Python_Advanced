from collections import deque

mg_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

max_caffeine = 300
initial_caffeine = 0

while mg_caffeine and energy_drinks:
    caffeine = mg_caffeine.pop()
    drink = energy_drinks.popleft()
    caff_day = caffeine * drink

    if caff_day + initial_caffeine <= max_caffeine:
        initial_caffeine += caff_day

    else:
        energy_drinks.append(drink)
        if initial_caffeine - 30 >= 0:
            initial_caffeine -= 30


if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {initial_caffeine} mg caffeine.')
