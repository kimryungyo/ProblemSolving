from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
grid = [ list(input()) for _ in range(n) ]

table = [ [1] * (m) for _ in range(n) ]

count = n * m
for y in range(1, n):
    for x in range(1, m):
        if grid[y-1][x] == grid[y][x-1]:
            if grid[y-1][x] != grid[y-1][x-1]:
                if grid[y-1][x-1] == grid[y][x]:

                    size = min(table[y - 1][x - 1], table[y - 1][x], table[y][x - 1]) + 1
                    table[y][x] = size

                    if size > 1: count += size - 1

print(count)