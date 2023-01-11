str1 = list(input())
new = []

for _ in range(len(str1)):
    new.append(str1.pop())

print("".join(new))