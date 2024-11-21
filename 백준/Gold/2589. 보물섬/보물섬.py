from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

dys = [0, 0, 1, -1]
dxs = [1, -1, 0, 0]

N, M = map(int, input().split())
grid = [ list(input()) for _ in range(N) ]

max_distnace = 0

for s_y in range(N):
    for s_x in range(M):
        if grid[s_y][s_x] == "W": continue

        visited = [ [ False ] * M for _ in range(N) ]
        visited[s_y][s_x] = True
        queue = deque( [ (s_y, s_x, 0) ])

        while queue:
            y, x, count = queue.popleft()
            if count > max_distnace:
                max_distnace = count

            for i in range(4):
                dy, dx = dys[i], dxs[i]
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == "L" and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append( (ny, nx, count + 1) )

print(max_distnace)