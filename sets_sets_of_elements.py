data = input().split(" ")
first_elem = {int(input()) for _ in range(int(data[0]))}
second_elem = {int(input()) for _ in range(int(data[1]))}

print(*first_elem.intersection(second_elem), sep="\n")
