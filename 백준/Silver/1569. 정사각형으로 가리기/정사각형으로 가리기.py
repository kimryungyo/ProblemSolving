from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
points = [ tuple(map(int, input().split())) for _ in range(n) ]

min_x, max_x, min_y, max_y = 1e10, -1e10, 1e10, -1e10

for point in points:
    x, y = point
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

length = max(max_x - min_x, max_y - min_y)

count_1, count_2 = 0, 0
for point in points:
    x, y = point
    if x in (min_x, min_x + length):
        if min_y <= y <= min_y + length:
            count_1 += 1
    elif y in (min_y, min_y + length):
        if min_x <= x <= min_x + length:
            count_1 += 1

for point in points:
    x, y = point
    if x in (max_x, max_x - length):
        if max_y - length <= y <= max_y:
            count_2 += 1
    elif y in (max_y, max_y - length):
        if max_x - length <= x <= max_x:
            count_2 += 1

if len(points) not in { count_1, count_2 }: print(-1)
else: print(length)