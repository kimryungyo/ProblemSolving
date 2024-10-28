from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
max_size = 0

points = []
for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append( point )

p_set = set(points)

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        a, b = points[i]
        c, d = points[j]

        dx = c - a
        dy = d - b

        new_p1 = (a + dy, b - dx)
        new_p2 = (c + dy, d - dx)

        if new_p1 in p_set:
            if new_p2 in p_set:
                size = (new_p1[0] - new_p2[0]) ** 2 + (new_p1[1] - new_p2[1]) ** 2
                if size > max_size: max_size = size

print(max_size)