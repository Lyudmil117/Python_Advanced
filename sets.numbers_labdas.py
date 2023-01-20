first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

function = {
    "Add First": lambda x: [first.add(int(el)) for el in x],
    "Add Second": lambda x: [second.add(int(el)) for el in x],
    "Remove First": lambda x: [first.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second.discard(int(el)) for el in x],
    "Check Subset": lambda:print(True) if first.issubset(second) or second.issubset(first) else print(False)
}

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)

    if data:
        function[command]([int(x) for x in data]) #ОБЪРНИ ВНИМАНИЕ ЧЕ ТЪВ СТАВА ТОВА С LIST COMPREHENSION
    else:
        function[command]()  # така викаш check subset(не е подаваш параметри затова така изглежда)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")