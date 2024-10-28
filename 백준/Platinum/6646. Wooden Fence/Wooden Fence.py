from itertools import combinations
from math import atan2, sqrt
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

def get_convex_hull(points):
    if len(points) < 2: return []
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

def get_convex_length(convex_hull):
    convex_length = len(convex_hull)
    if convex_length < 2: return 0

    length = 0
    for i in range(convex_length - 1):
        p1, p2 = convex_hull[i], convex_hull[i + 1]
        length += sqrt(get_length(p1, p2))

    p1, p2 = convex_hull[0], convex_hull[-1]
    length += sqrt(get_length(p1, p2))

    return length

def print_answer(value):
    print(f"The lost value is {value}.")

while True:
    N = int(input())
    if not N: break

    trees = [ tuple(map(int, input().split())) for _ in range(N) ]
    trees_set = set(trees)
    minimum_lost = float("inf")

    for logging_count in range(1, N):
        for loggings in combinations(range(N), logging_count):
            logged_trees = { trees[i] for i in loggings }
            remain_trees = trees_set - logged_trees

            maked_fence = sum(tree[3] for tree in logged_trees)
            losted_value = sum(tree[2] for tree in logged_trees)

            convex_hull = get_convex_hull([ (x, y) for x, y, _, _ in remain_trees ])
            fence_length = get_convex_length(convex_hull)

            if maked_fence >= fence_length and losted_value < minimum_lost:
                minimum_lost = losted_value

    print_answer(minimum_lost)