from sys import stdin
input = stdin.readline

N = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    arr[i][1:] = map(int, input().split())
q = int(input())
check = [tuple(map(int, input().split())) for _ in range(q)]
check.append((N, N))

check.sort()
memo = [[0] * (N + 1) for _ in range(N + 1)]

sx, sy = 1, 1
result = arr[1][1]
failed = False

for ex, ey in check:
    if sx > ex or sy > ey:
        result = -1
        break

    memo[sx][sy] = 0
    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            if (x != sx) or (y != sy):
                memo[x][y] = 0
            if y - 1 >= sy:
                memo[x][y] = max(memo[x][y], arr[x][y] + memo[x][y - 1])
            if x - 1 >= sx:
                memo[x][y] = max(memo[x][y], arr[x][y] + memo[x - 1][y])

    result += memo[ex][ey]
    sx, sy = ex, ey

print(result)