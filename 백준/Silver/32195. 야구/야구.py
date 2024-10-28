from bisect import bisect_right
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
balls = []
fouls = 0
for _ in range(N):
    x, y = map(int, input().split())

    if y >= x and y >= -x:
        distance = x ** 2 + y ** 2
        balls.append( distance )

    else: fouls += 1

balls.sort()

Q = int(input())
for _ in range(Q):
    R = int(input()) ** 2

    homeruns = bisect_right(balls, R)
    counts = [fouls, homeruns, N - fouls - homeruns]
    print(" ".join(map(str, counts)))