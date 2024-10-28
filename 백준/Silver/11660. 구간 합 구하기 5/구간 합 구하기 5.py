from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int ,input().split())
grid = [ list(map(int, input().split())) for _ in range(N) ]
table = [ [0] * (N + 1) for _ in range(N + 1) ]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        
        if x == 0 or y == 0:
            table[y][x] = grid[y-1][x-1]
            continue

        sum = grid[y-1][x-1] + table[y-1][x] + table[y][x-1] - table[y-1][x-1]
        table[y][x] = sum
        
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    sum = table[y2][x2] - table[y2][x1-1] - table[y1-1][x2] + table[y1-1][x1-1]
    print(sum)