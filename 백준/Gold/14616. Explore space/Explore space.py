from fractions import Fraction
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
ranges = []
for num in range(n):
    a, b, c, d = map(int, input().split())
    slope1 = Fraction(b, a)
    slope2 = Fraction(d, c)
    mini, maxi = sorted([slope1, slope2])
    ranges.append((mini, False, False, num))
    ranges.append((maxi, True, True, num))

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    slope = Fraction(b, a)
    ranges.append((slope, True, False, None))

ranges.sort()

active = set()
removed = set()
radiation = n

for point in ranges:
    pos, type, raser, num = point
    if num in removed: continue

    if type is False: active.add(num)
    else:
        if raser is False:
            radiation -= len(active)
            removed |= active
            active = set()

        else: active.remove(num)

print(radiation)