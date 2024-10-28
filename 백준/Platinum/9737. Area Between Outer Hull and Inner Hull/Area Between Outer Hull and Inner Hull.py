from math import sqrt, pi, atan2, acos 
from collections import deque
from sys import stdin
input = stdin.readline

def shoelace_area(points):
    n = len(points)
    area = 0
    
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    
    return abs(area) / 2

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

    base = min(points, key=lambda p: (p[1], p[0]))

    points_weights = sorted(map(point_weight, points), key=lambda x: (x[0], x[1]))
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

while True:
    ID, N = input().split()
    if ID == "ZZ": break
    points = { tuple(map(float, input().split())) for _ in range(int(N)) }

    out_convex_hull = get_convex_hull(points)
    out_convex_hull_area = shoelace_area(out_convex_hull)

    points -= set(out_convex_hull)
    in_convex_hull = get_convex_hull(points)
    in_convex_hull_area = shoelace_area(in_convex_hull)

    area = out_convex_hull_area - in_convex_hull_area
    print(f"ProblemID {ID}: {area:.4f}")