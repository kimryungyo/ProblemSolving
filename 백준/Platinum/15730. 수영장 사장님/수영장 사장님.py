from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]

water = 10 ** 10
queue = []
for y in range(N):
    for x in range(M):
        if y == 0 or y == N-1 or x == 0 or x == M-1:
            h = grid[y][x]
            heappush(queue, (h, y, x))
            visited[y][x] = True
            if h < water: water = h

answer = 0
while queue:
    h, y, x = heappop(queue)

    answer += max(0, water - h)
    if h > water: water = h

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            heappush(queue, (grid[ny][nx], ny, nx))

print(answer)