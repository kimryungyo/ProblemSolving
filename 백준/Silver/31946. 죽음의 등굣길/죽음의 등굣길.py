from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
X = int(input())

if grid[0][0] != grid[N-1][M-1]:
    print("DEAD")
    quit()

visited = [[False]*M for _ in range(N)]
visited[0][0] = True
queue = deque([(0,0)])
color = grid[0][0]

while queue:
    r, c = queue.popleft()
    if r == N-1 and c == M-1:
        print("ALIVE")
        quit()
        
    for nr in range(max(0, r - X), min(N, r + X + 1)):
        dist_r = abs(nr - r)
        limit_c = X - dist_r
        cmin = max(0, c - limit_c)
        cmax = min(M, c + limit_c + 1)
        
        for nc in range(cmin, cmax):
            if not visited[nr][nc] and grid[nr][nc] == color:
                visited[nr][nc] = True
                queue.append((nr,nc))

print("DEAD")