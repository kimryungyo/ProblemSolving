from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
table = [ list(map(int, input().split())) for _ in range(N) ]
ds = [-1, 0, 1]

mountain_count = 0
points = set()
for y in range(N):
    for x in range(M):
        points.add((y, x))

while points:
    root = points.pop()
    r_y, r_x = root
    height = table[r_y][r_x]
    queue = deque([root])
    is_mountain = True

    while queue:
        y, x = queue.popleft()

        for dx in ds:
            for dy in ds:
                n_y, n_x = y + dy, x + dx
                if 0 <= n_y < N and 0 <= n_x < M:
                    next = (n_y, n_x)
                    if table[n_y][n_x] == height:
                        if next in points:
                            points.remove(next)
                            queue.append(next)
                    elif table[n_y][n_x] > height:
                        is_mountain = False

    if is_mountain:
        mountain_count += 1

print(mountain_count)