import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    maps[x][y] = 0
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1:
            count += dfs(nx, ny)

    return count

counts = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            counts.append(dfs(i, j))

print(len(counts))
for count in sorted(counts):
    print(count)