from random import randint
from collections import deque
from sys import stdin

def get_convex_hull(n, points):
    from functools import cmp_to_key

    def ccw(p, p1, p2):
        x1, y1 = [p1[0] - p[0], p1[1] - p[1]]
        x2, y2 = [p2[0] - p[0], p2[1] - p[1]]
        return x1*y2 - x2*y1

    def compare_dist(p1, p2):
        d1 = p1[0]**2 + p1[1]**2
        d2 = p2[0]**2 + p2[1]**2
        return d1 > d2

    def comp(p1, p2):
        direction = ccw([0, 0], p1, p2)
        if direction > 0:
            return -1
        if direction == 0:
            if compare_dist(p1, p2):
                return 1
            else:
                return -1
        if direction < 0:
            return 1

    points = sorted(points, key=lambda x: (x[1], x[0]))
    start = points[0]

    shifted_points = [[x-start[0], y-start[1]] for x, y in points[1:]]
    sorted_shifted_points = sorted(shifted_points, key= cmp_to_key(comp))
    points = [[x+start[0], y+start[1]] for x, y in sorted_shifted_points]

    stack = [start, points[0]]

    for p in points[1:]:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <=0:
            stack.pop()
        stack.append(p)

    return start, stack



def solution():
    from fractions import Fraction
    from math import atan2
    input = stdin.readline

    N = int(input())
    if N < 3: return 0

    points = [ tuple(map(int, input().split())) for _ in range(N) ]
    base, convex_hull = get_convex_hull(N, points)

    length = len(convex_hull)
    if length < 3: return 0

    top_y = max(point[1] for point in convex_hull)
    bottom_y = min(point[1] for point in convex_hull)
    height = top_y - bottom_y

    convex_hull.append(base)

    rectangle = [ None, None ]

    right = True
    min_area = float("inf")
    for idx in range(length):
        p1, p2 = convex_hull[idx], convex_hull[idx + 1]
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x1 - x2, y1 - y2

        if dx == 0:
            bottom_x = top_x = x1

        else:
            slope = Fraction(dy, dx)
            if slope == 0: continue

            dy_lower, dy_upper = bottom_y - y1, top_y - y1

            bottom_x = Fraction(x1) + (Fraction(dy_lower) / slope)
            top_x = Fraction(x1) + (Fraction(dy_upper) / slope)
            
        start_x = -1e10 if right else 1e10
        area = abs((start_x * 2) - bottom_x - top_x) * height

        if area < min_area:
            min_area = area
            rectangle[int(right)] = (bottom_x, top_x)

        if p2[1] == top_y:
            right = False
            min_area = float("inf")

    left_bottom, left_top = rectangle[0]
    right_bottom, right_top = rectangle[1]

    area = ( (right_bottom - left_bottom) + (right_top - left_top) ) * height / 2

    return float(area)

print(solution())