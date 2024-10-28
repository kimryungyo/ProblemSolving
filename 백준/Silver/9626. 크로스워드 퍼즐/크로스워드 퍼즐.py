M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

total_M = M + U + D
total_N = N + L + R

puzzle = []
for _ in range(M):
    row = list(input())
    puzzle.append(row)

for i in range(total_M):
    row = []
    for j in range(total_N):
        if i < U or i >= U+M or j < L or j >= L+N:
            row.append('#' if (i+j)%2 == 0 else '.')
        else:
            row.append(puzzle[i-U][j-L])
    print(''.join(row))