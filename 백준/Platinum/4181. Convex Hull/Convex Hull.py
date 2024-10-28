from fractions import Fraction
from sys import stdin
input = stdin.readline

def get_info(point):
    x, y = point
    dx, dy = x - base_x, y - base_y
    distance = dx ** 2 + dy ** 2

    if dx != 0: slope = Fraction(dy, dx)
    elif dy > 0: slope = 1e18
    else: slope = -1e18
    return (slope, distance, point)

N = int(input())
points = [ input().split() for _ in range(N) ]
convex_hull = [ [int(p[0]), int(p[1])] for p in points if p[2] == "Y" ]
print(len(convex_hull))

base = min(convex_hull, key=lambda p: (p[0], p[1]))
base_x, base_y = base
convex_hull.remove(base)
print(base_x, base_y)

info_convex_hull = list(map(get_info, convex_hull))
sorted_convex_hull = sorted(info_convex_hull)

grouped_convex_hull = [ ]
for slope, distance, point in sorted_convex_hull:

    if (not grouped_convex_hull) or (grouped_convex_hull[-1][0] != slope):
        grouped_convex_hull.append( [ slope, [ [distance, point] ] ] )
        continue

    grouped_convex_hull[-1][1].append( [distance, point] )

groups_count = len(grouped_convex_hull)
for num in range(groups_count):
    reverse = (num == groups_count - 1)
    group = sorted(grouped_convex_hull[num][1], reverse=reverse)
    for distance, (x, y) in group:
        print(x, y)