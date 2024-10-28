from math import atan2
from collections import deque
from sys import stdin
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

def point_weight(point):
    angle = get_angle(base, point)
    length = get_length(base, point)
    return (angle, length, point)

N, M = map(int, input().split())
A_points = [ tuple(map(int, input().split())) for _ in range(N) ]
B_points = [ tuple(map(int, input().split())) for _ in range(M) ]

points = { (A_points[i][0] + B_points[j][0], A_points[i][1] + B_points[j][1]) for j in range(M) for i in range(N) }

base = min(points, key=lambda p: p[1] * 1e5 + p[0])

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

print(len(convex_hull))

base = min(convex_hull, key=lambda p: (p[0], p[1]))
base_idx = convex_hull.index(base)

for i in range(base_idx, len(convex_hull)):
    print(convex_hull[i][0], convex_hull[i][1])

for i in range(0, base_idx):
    print(convex_hull[i][0], convex_hull[i][1])