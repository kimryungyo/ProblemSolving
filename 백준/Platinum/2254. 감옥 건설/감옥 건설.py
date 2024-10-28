from math import atan2
from collections import deque
from sys import stdin
input = stdin.readline

def get_ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def get_ccw_sign(p1, p2, p3):
    ccw = get_ccw(p1, p2, p3)
    if ccw == 0: return 0
    elif ccw > 0: return 1
    else: return -1

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

def is_point_in_convex(point, convex):
    sign = None

    convex_1 = convex[0]
    for i in range(1, len(convex)):
        convex_2 = convex[i]
        ccw_sign = get_ccw_sign(convex_1, convex_2, point)
        if sign is None: sign = ccw_sign
        elif sign != ccw_sign: return False
        convex_1 = convex_2

    ccw_sign = get_ccw_sign(convex[-1], convex[0], point)
    if sign != ccw_sign: return False

    return True

def get_convex_hull(N, points):
    base = min(points, key=lambda p: p[1] * 1e5 + p[0])

    def point_weight(point):
        angle = get_angle(base, point)
        length = get_length(base, point)
        return (angle, length, point)
    
    points_weights = sorted(map(point_weight, points), key=lambda x: int(x[0] * 1e32) + x[1])
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

N, Px, Py = map(int, input().split())
points = { tuple(map(int, input().split())) for _ in range(N) }

count = 0
while len(points) >= 3:
    convex_hull = get_convex_hull(None, points)
    if is_point_in_convex((Px, Py), convex_hull):
        count += 1
        for point in convex_hull:
            points.remove(point)
    else: break

print(count)