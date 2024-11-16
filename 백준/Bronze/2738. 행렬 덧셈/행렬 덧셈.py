N, M = map(int, input().split())

matrix_A = [list(map(int, input().split())) for _ in range(N)]
matrix_B = [list(map(int, input().split())) for _ in range(N)]
result_matrix = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(matrix_A[i][j] + matrix_B[i][j])
    result_matrix.append(row)

for row in result_matrix:
    print(' '.join(map(str, row)))