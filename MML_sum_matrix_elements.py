rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_nums = 0

for i in range(rows):
    current_line = [int(x) for x in input().split(", ")]
    matrix.append(current_line)
    sum_nums += sum(current_line)

print(sum_nums)
print(matrix)
