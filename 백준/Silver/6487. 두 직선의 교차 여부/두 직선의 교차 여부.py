from sys import stdin
input = lambda: stdin.readline().rstrip()
from decimal import Decimal

class Point:
    def __init__(self, point):
        x, y = point
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __gt__(self, other):
        return other < self

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    a, b, c, d = Point(nums[0:2]), Point(nums[2:4]), Point(nums[4:6]), Point(nums[6:8])

    if (a.y - b.y) * (c.x - d.x) != (c.y - d.y) * (a.x - b.x):
        print("POINT", end=' ')
        t = Decimal((d.y - c.y) * (a.x - c.x) - (d.x - c.x) * (a.y - c.y)) / Decimal((b.y - a.y) * (d.x - c.x) - (b.x - a.x) * (d.y - c.y))
        print(f"{(b.x - a.x) * t + a.x:.2f} {(b.y - a.y) * t + a.y:.2f}")
    elif c.y * (a.x - b.x) != (a.y - b.y) * (c.x - a.x) + a.y * (a.x - b.x):
        print("NONE")
    else:
        print("LINE")