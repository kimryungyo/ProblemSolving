from fractions import Fraction
from sys import stdin
input = stdin.readline

N = int(input())
slope_counts = { None: 0 }
slopes = []
total_count = N
for _ in range(N):
    dx, dy = map(int, input().split())

    if dx == dy == 0:
        slope_counts[None] += 1
        slopes.append(None)
        continue

    if dx == 0: slope = "inf"
    else: slope = Fraction(dy, dx)

    if slope not in slope_counts:
        slope_counts[slope] = 0
    slope_counts[slope] += 1
    slopes.append(slope)

count = 0
for slope in slopes:
    slope_counts[slope] -= 1
    total_count -= 1

    if slope is None:
        count += total_count

    else:
        if slope == "inf": reverse_slope = Fraction(0)
        elif slope == Fraction(0): reverse_slope = "inf"
        else: 
            nume, deno = slope.numerator, slope.denominator
            reverse_slope = Fraction(-deno, nume)
            
        count += slope_counts.get(reverse_slope, 0)
        count += slope_counts[None]

print(count)