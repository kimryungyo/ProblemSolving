from sys import stdin
from collections import deque

input = stdin.readline

M, N = map(int, input().split())
tomatoes = []
queue = deque()

for i in range(N):
    row = list(map(int, input().split()))
    tomatoes.append(row)
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dxs[k]
        ny = y + dys[k]
        if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = tomatoes[x][y] + 1
            queue.append((nx, ny))

result = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            quit()
        result = result if result > tomatoes[i][j] else tomatoes[i][j]

print(result - 1)