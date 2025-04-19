from sys import stdin
input = stdin.readline

M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
areas = []

for y in range(M):
    for x in range(N):
        if grid[y][x] == 0:
            stack = [(x, y)]
            grid[y][x] = 1
            area = 0
            while stack:
                cx, cy = stack.pop()
                area += 1
                for dx, dy in dirs:
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < N and 0 <= ny < M and grid[ny][nx] == 0:
                        grid[ny][nx] = 1
                        stack.append((nx, ny))
            areas.append(area)

areas.sort()
print(len(areas))
print(*areas)