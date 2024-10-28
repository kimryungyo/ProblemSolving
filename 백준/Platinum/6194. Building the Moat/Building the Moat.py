from collections import deque
from sys import stdin
from math import atan2, sqrt
input = stdin.readline

def get_ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def get_length(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    length = dx ** 2 + dy ** 2
    return length

def get_angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    angle = atan2(dy, dx)
    return angle

def get_convex_hull(points):
    def point_weight(point):
        angle = get_angle(base, point)
        length = get_length(base, point)
        return (angle, length, point)

    base = min(points, key=lambda p: p[1] * 1e5 + p[0])

    points_weights = sorted(map(point_weight, points), key=lambda x: int(x[0] * 1e22) + x[1])
    candidates = deque()
    before_angle = None
    for angle, length, point in points_weights:
        if angle == before_angle: candidates.pop()
        candidates.append(point)
        before_angle = angle
    if candidates[0] == base: candidates.popleft()

    second = candidates.popleft()
    convex_hull = [ base, second ]

    while candidates:
        point = candidates.popleft()
        convex_hull.append(point)
        get_convex_ccw = lambda: get_ccw(convex_hull[-3], convex_hull[-2], convex_hull[-1])
        while get_convex_ccw() <= 0: 
            convex_hull.pop(-2)

    return convex_hull

def get_convex_length(convex_hull):
    convex_length = len(convex_hull)
    convex_hull.append(convex_hull[0])

    length = 0
    for i in range(convex_length):
        p1, p2 = convex_hull[i], convex_hull[i + 1]
        length += sqrt(get_length(p1, p2))

    return length

N = int(input())
points = [ tuple(map(int, input().split())) for _ in range(N) ]
convex_hull = get_convex_hull(points)
convex_length = get_convex_length(convex_hull)
print(f"{convex_length:.2f}")