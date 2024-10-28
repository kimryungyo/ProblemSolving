from fractions import Fraction
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
ranges = []
for _ in range(N):
    xbl, ybl, xtr, ytr = map(int, input().split())
    end_slope = Fraction(ytr, xbl)
    start_slope = Fraction(ybl, xtr)

    ranges.append( (start_slope, 0) )
    ranges.append( (end_slope, 1) )
ranges.sort()

active = 0
max_active = 0
for slope, event in ranges:
    if event: active -= 1
    else:
        active += 1
        if active > max_active:
            max_active = active

print(max_active)