import sys
import math

input = sys.stdin.readline

def gcd(a, b):
    return math.gcd(a, b)

def normalize_line(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = x2*y1 - x1*y2

    if A < 0 or (A == 0 and B < 0) or (A == 0 and B == 0 and C < 0):
        A, B, C = -A, -B, -C

    g = gcd(abs(A), gcd(abs(B), abs(C)))
    if g != 0:
        A //= g
        B //= g
        C //= g

    return (A, B, C)

def normalize_direction(dx, dy):
    if dx == 0 and dy == 0:
        return (0, 0)
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy
    return (dx, dy)

def dot(ax, ay, bx, by):
    return ax*bx + ay*by

N = int(input())

lines_map = {}

for _ in range(N):
    x1f, y1f, x2f, y2f = input().split()
    x1 = int(round(float(x1f)*100))
    y1 = int(round(float(y1f)*100))
    x2 = int(round(float(x2f)*100))
    y2 = int(round(float(y2f)*100))
    A, B, C = normalize_line(x1, y1, x2, y2)
    lines_map.setdefault((A,B,C), []).append((x1, y1, x2, y2))

answer = 0

for (A,B,C), segments in lines_map.items():
    x0, y0, x1_, y1_ = segments[0]
    dx0 = x1_ - x0
    dy0 = y1_ - y0
    dx0, dy0 = normalize_direction(dx0, dy0)
    intervals = []
    for (sx1, sy1, sx2, sy2) in segments:
        d1 = dot(sx1 - x0, sy1 - y0, dx0, dy0)
        d2 = dot(sx2 - x0, sy2 - y0, dx0, dy0)
        t1, t2 = min(d1, d2), max(d1, d2)
        intervals.append((t1, t2))
    intervals.sort(key=lambda x: x[0])
    merged_count = 0
    current_end = None
    for st, en in intervals:
        if current_end is None:
            merged_count += 1
            current_end = en
        else:
            if st <= current_end:
                if en > current_end:
                    current_end = en
            else:
                merged_count += 1
                current_end = en
    answer += merged_count

print(answer)