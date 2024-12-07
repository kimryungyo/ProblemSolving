from bisect import bisect_left
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

titles = []
limits = []

for _ in range(N):
    title, limit = input().split()
    titles.append(title)
    limits.append(int(limit))

for _ in range(M):
    power = int(input())
    index = bisect_left(limits, power)
    print(titles[index])