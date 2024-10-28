from math import comb
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(comb(m, n))