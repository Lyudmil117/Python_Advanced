matrix = []
rows = int(input())
wanted = []

for _ in range(rows):
    line = [int(x) for x in input().split(" ")]
    matrix.append(line)

for i in range(len(matrix)):
    wanted.append(matrix[i][i]) # така въртиш по матрицата и взимаш 0,0 ; 1,1  ; 2,2 (тва са индексите на елементите на марицата)

print(sum(wanted))
