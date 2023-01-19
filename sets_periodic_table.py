n = int(input())
elements = set()
for _ in range(n):
    data = input().split(" ")
    for item in data:
        elements.add(item)
print(*elements, sep="\n")

