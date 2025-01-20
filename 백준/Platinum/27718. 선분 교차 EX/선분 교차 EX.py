from sys import stdin
input = stdin.readline

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def on_segment(ax, ay, bx, by, px, py):
    if ccw(ax, ay, bx, by, px, py) != 0:
        return False
    return min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)

def collinear_overlap(seg1, seg2):
    a1, b1, a2, b2 = seg1
    c1, d1, c2, d2 = seg2

    if (a1, b1) > (a2, b2):
        a1, b1, a2, b2 = a2, b2, a1, b1
    if (c1, d1) > (c2, d2):
        c1, d1, c2, d2 = c2, d2, c1, d1

    if (a2, b2) < (c1, d1) or (c2, d2) < (a1, b1):
        return '0'

    if (a2, b2) == (c1, d1) or (c2, d2) == (a1, b1):
        return '1'

    return '3'

def intersect_type(seg1, seg2):
    a1, b1, a2, b2 = seg1
    c1, d1, c2, d2 = seg2

    if seg1 == seg2:
        return '3'

    ccw1 = ccw(a1, b1, a2, b2, c1, d1)
    ccw2 = ccw(a1, b1, a2, b2, c2, d2)
    ccw3 = ccw(c1, d1, c2, d2, a1, b1)
    ccw4 = ccw(c1, d1, c2, d2, a2, b2)

    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        return collinear_overlap(seg1, seg2)

    if (ccw1 * ccw2 < 0) and (ccw3 * ccw4 < 0):
        return '2'

    if on_segment(a1, b1, a2, b2, c1, d1) or on_segment(a1, b1, a2, b2, c2, d2) or \
       on_segment(c1, d1, c2, d2, a1, b1) or on_segment(c1, d1, c2, d2, a2, b2):
        return '1'

    return '0'

for i in range(N):
    seg1 = segments[i]
    for j in range(N):
        if i == j:
            print('3', end='')
        else:
            seg2 = segments[j]
            print(intersect_type(seg1, seg2), end='')
    print()