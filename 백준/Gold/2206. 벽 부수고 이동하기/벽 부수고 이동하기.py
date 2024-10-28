from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
if N == M == 1: print(1); quit()
maps = [ list(map(int, input())) for _ in range(N) ]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

visited = [ [[False, False] for _ in range(M) ] for _ in range(N) ]
visited[0][0][0] = True

queue = deque([ ((0, 0), 0, False) ])

while queue:
    pos, moved, broken = queue.popleft()
    broken_int = int(broken)
    y, x = pos
    moved += 1
    
    for i in range(4):
        dy, dx = dys[i], dxs[i]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:

            if ny == N-1 and nx == M-1:
                print(moved + 1)
                quit()

            if visited[ny][nx][broken_int] is False:

                next = (ny, nx)

                if maps[ny][nx] == 0:
                    queue.append( (next, moved, broken) )
                    visited[ny][nx][broken_int] = True

                elif broken is False:
                    queue.append( (next, moved, True) )
                    visited[ny][nx][1] = True

print(-1)