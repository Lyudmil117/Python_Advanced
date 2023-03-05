num = int(input())
matrix = []
result_list = []

for row in range(num):
    line = [int(elem) for elem in input().split(", ")]
    matrix.append(line)

result_list = [elem for row in matrix for elem in row]
print(result_list)
