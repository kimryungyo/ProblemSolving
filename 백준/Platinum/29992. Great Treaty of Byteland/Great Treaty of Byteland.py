from sys import stdin
input = stdin.readline

def get_convex_hull(points):
    if len(points) <= 1:
        return points

    points = sorted(points, key=lambda p: (p[0], p[1]))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - \
               (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    convex = lower[:-1] + upper[:-1]

    unique_convex = []
    seen = set()
    for p in convex:
        if (p[0], p[1]) not in seen:
            unique_convex.append(p)
            seen.add((p[0], p[1]))
    return unique_convex

N = int(input())
points = [ tuple(map(int, input().split())) for _ in range(N) ]
convex_hull = get_convex_hull(points)
set_convex_hull = set(convex_hull)

for i in range(N):
    if points[i] in set_convex_hull:
        print(i + 1, end = " ")