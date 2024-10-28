from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
grid = [ list(map(int, input())) for _ in range(n) ]

table = [ [0] * (m + 1) for _ in range(n + 1) ]

max_size = 0
for y in range(1, n + 1):
    for x in range(1, m + 1):
        if grid[y-1][x-1] == 1:
            size = min(table[y - 1][x - 1], table[y - 1][x], table[y][x - 1]) + 1
            table[y][x] = size
            if size > max_size:
                max_size = size

        else:
            table[y][x] = 0

print(max_size ** 2)