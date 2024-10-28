from fractions import Fraction
from sys import stdin
input = lambda: stdin.readline()

N = int(input())

slopes = set()
for _ in range(N):
    x, y = map(int, input().split())

    if x == 0:
        if y > 0: slopes.add(0)
        else: slopes.add(1)
        continue

    elif y == 0:
        if x > 0: slopes.add(2)
        else: slopes.add(3)
        continue

    ops = -1
    
    if x > 0:
        if y > 0: ops = 0
        else: ops = 1

    else:
        if y > 0: ops = 2
        else: ops = 3

    slopes.add((Fraction(y, x), ops))

print(len(slopes))