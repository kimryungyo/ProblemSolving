from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [ list(input()) for _ in range(N) ]

for i in range(N):
    for j in range(M):
        if grid[i][j] != '.':
            grid[i][M-j-1] = grid[i][j]

for i in range(N): 
    print(''.join(grid[i]))