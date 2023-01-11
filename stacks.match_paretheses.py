data = input()
lst1 = []

for i in range(len(data)):
    char = data[i]

    if char == "(":
        lst1.append(i)
    elif char == ")":
        start = lst1.pop()
        wanted = data[start:i + 1]
        print(wanted)

