matrix = []
rows, cols = [int(x) for x in input().split(", ")]

for _ in range(rows):
    line = [int(x) for x in input().split(" ")]
    matrix.append(line)

result = []

for col in range(cols): #6
    column_sum = 0

    for row in range(rows): #3
        column_sum += matrix[row][col]

    result.append(column_sum)

print(*result, sep="\n")