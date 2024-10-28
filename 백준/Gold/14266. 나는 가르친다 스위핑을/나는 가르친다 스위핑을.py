from fractions import Fraction
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
ranges = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    slope1 = Fraction(b, a)
    slope2 = Fraction(d, c)
    mini, maxi = sorted([slope1, slope2])
    ranges.append((mini, False))
    ranges.append((maxi, True))

ranges.sort(key=lambda x: x[0] * Fraction(10 ** 10) + x[1])

active = 0
max_active = 0

for point in ranges:
    pos, type = point

    if type is False: active += 1
    else:
        if active > max_active:
            max_active = active
        active -= 1

print(max_active)