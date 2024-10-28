def get_convex_hull(n, points):
    from functools import cmp_to_key

    def compare_dist(p1, p2):
        d1 = p1[0] ** 2 + p1[1] ** 2
        d2 = p2[0] ** 2 + p2[1] ** 2
        return d1 > d2

    def comp(p1, p2):
        direction = get_ccw([0, 0], p1, p2)
        if direction > 0: return -1
        if direction == 0:
            if compare_dist(p1, p2): return 1
            else: return -1
        if direction < 0: return 1

    points = sorted(points, key=lambda x: (x[1], x[0]))
    start = points[0]

    shifted_points = [ [x - start[0], y - start[1] ] for x, y in points[1:]]
    sorted_shifted_points = sorted(shifted_points, key=cmp_to_key(comp))
    points = [ [ x + start[0], y + start[1] ] for x, y in sorted_shifted_points]

    stack = [ start, points[0] ]

    for p in points[1:]:
        while len(stack) > 1 and get_ccw(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

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

def is_point_in_convex(point, convex):
    sign = None

    convex_1 = convex[0]
    for i in range(1, len(convex)):
        convex_2 = convex[i]
        ccw_sign = get_ccw_sign(convex_1, convex_2, point)
        if ccw_sign == 0: return False
        if sign is None: sign = ccw_sign
        elif sign != ccw_sign: return False
        convex_1 = convex_2

    ccw_sign = get_ccw_sign(convex[-1], convex[0], point)
    if sign != ccw_sign: return False

    return True

from sys import stdin
input = stdin.readline

N = int(input())
if N < 2: print("Yes"); quit()

points = [ tuple(map(int, input().split())) for _ in range(N) ]

convex_hull = get_convex_hull(N, points)
if is_point_in_convex((0, 0), convex_hull):
    print("No")
else:
    print("Yes")