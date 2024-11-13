from collections import deque
from sys import stdin 
input = stdin.readline

dys = [0, 0, 1, -1]
dxs = [1, -1, 0, 0]

N = int(input())
grid = [ list(map(int, input().split())) for _ in range(N) ]

max_groups = 0
for height in range(0, 101):
    waters = set()
    for y in range(N):
        for x in range(N):
            if grid[y][x] >= height:
                waters.add( (y, x) )

    groups = 0
    while waters:
        groups += 1
        union = waters.pop()
        queue = deque( [union] )

        while queue:
            pos = queue.popleft()
            y, x = pos

            for i in range(4):
                dy, dx = dys[i], dxs[i]
                ny, nx = y + dy, x + dx

                n_pos = (ny, nx)
                if n_pos in waters:
                    waters.remove(n_pos)
                    queue.append(n_pos)

    if groups > max_groups:
        max_groups = groups

print(max_groups)