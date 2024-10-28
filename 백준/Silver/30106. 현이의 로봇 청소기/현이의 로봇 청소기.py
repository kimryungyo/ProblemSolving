from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 6)
input = stdin.readline

N, M, K = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and abs(heights[x][y] - heights[nx][ny]) <= K:
            dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)