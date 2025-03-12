from sys import stdin
input = lambda: stdin.readline().rstrip()

def check_is_around(y, x):
    if x == 0 or x == N - 1:
        return True
    if y == 0 or y == N - 1:
        return True
    return False

def loop_around(y, x):
    arounds = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == dx == 0: continue
            ny, nx = y + dy, x + dx
            if check_is_around(ny, nx):
                arounds.append( (ny, nx, grid[ny][nx]) )
    return arounds

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [ list(input()) for _ in range(N) ]
    if N < 3: print(0); continue

    for y in range(N):
        for x in range(N):
            if grid[y][x] != "#":
                grid[y][x] = int(grid[y][x])

    for y in range(N):
        for x in range(N):
            if not check_is_around(y, x):
                arounds = loop_around(y, x)
                if not arounds:
                    grid[y][x] = "*"
                else:
                    mins = min(arounds, key=lambda x: x[2])[2]
                    if mins:
                        grid[y][x] = "*"
                        for cy, cx, count in arounds:
                            grid[cy][cx] -= 1

    answer = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == "*":
                answer += 1

    print(answer)