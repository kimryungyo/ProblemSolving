from sys import stdin
input = lambda: stdin.readline().rstrip()

h, w, n = map(int, input().split())
points = { tuple(map(int, input().split())) for _ in range(n) }

pos =  [
    [0, 0], [1, 0], [2, 0],
    [0, 1], [1, 1], [2, 1],
    [0, 2], [1, 2], [2, 2],
]

def check(x, y):
    new_pos = []
    for pixel in pos:
        dx, dy = pixel
        new_pos.append([x + dx, y + dy])
    return new_pos

moves = []
for i in range(3):
    for j in range(3):
        new = check(-i, -j)
        moves.append(new)

checks = set()
for point in points:
    y, x = point
    for move in moves:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= w - 2 and 1 <= ny <= h - 2:
                checks.add( (ny, nx) )

def check_point(y, x):
    count = 0
    for dx, dy in pos:
        nx, ny = x + dx, y + dy
        if (ny, nx) in points:
            count += 1
    return count

results = [ 0 ] * 10
results[0] = (h - 2) * (w - 2)
for y, x in checks:
    count = check_point(y, x)
    if count > 0:
        results[count] += 1
        results[0] -= 1

print(*results, sep = "\n")