n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

first_diagonal = [matrix[r][r] for r in range(n)]
second_diagonal = [matrix[r][n - r - 1] for r in range(n - 1, -1, -1)]

print(f'Primary diagonal: {", ".join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}')
print(f'Secondary diagonal: {" ,".join(str(x) for x in second_diagonal)[::-1]}. Sum: {sum(second_diagonal)}')

