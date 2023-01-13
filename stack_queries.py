stack = []
n = int(input())

for _ in range(n):
    data = input().split(" ")
    action = data[0]

    if action == "1":
        number = int(data[1])
        stack.append(number)
    elif action == "2":
        stack.pop()
    elif action == "3":
        print(max(stack))
    elif action == "4":
        print(min(stack))

stack.reverse()
print(*stack, sep=", ")   # с ("*" stack) разопаковам стака и го отпечатвам после на един ред
