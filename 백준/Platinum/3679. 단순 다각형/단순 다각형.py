from fractions import Fraction
from sys import stdin
input = stdin.readline

def main():

    def get_info(point):
        x, y = point
        dx, dy = x - base_x, y - base_y
        distance = dx ** 2 + dy ** 2

        if dx != 0: slope = Fraction(dy, dx)
        elif dy > 0: slope = 1e18
        else: slope = -1e18

        return (slope, distance, point)

    N, *values = map(int, input().split())
    points = [ tuple(values[i:i+2]) for i in range(0, N * 2, 2) ]
    indexs = { value: index for index, value in enumerate(points) }
    convex_hull = points.copy()

    base = min(convex_hull, key=lambda p: (p[0], p[1]))
    base_x, base_y = base
    convex_hull.remove(base)

    info_convex_hull = list(map(get_info, convex_hull))
    sorted_convex_hull = sorted(info_convex_hull, reverse=True)

    grouped_convex_hull = [ ]
    for slope, distance, point in sorted_convex_hull:

        if (not grouped_convex_hull) or (grouped_convex_hull[-1][0] != slope):
            grouped_convex_hull.append( [ slope, [ [distance, point] ] ] )
            continue

        grouped_convex_hull[-1][1].append( [distance, point] )

    print(indexs[base], end = " ")
    groups_count = len(grouped_convex_hull)
    for num in range(groups_count):
        reverse = (num == groups_count - 1)
        group = sorted(grouped_convex_hull[num][1], reverse=reverse)
        for distance, point in group:
            print(indexs[point], end = " ")

    print()

T = int(input())
for _ in range(T): main()