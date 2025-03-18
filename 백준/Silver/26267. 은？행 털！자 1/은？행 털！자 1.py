from sys import stdin

input = lambda: stdin.readline().rstrip()
N = int(input())
dct = {}

for _ in range(N):
    x, t, c = map(int, input().split())
    diff = x - t
    if diff in dct:
        dct[diff] += c
    else:
        dct[diff] = c

print(max(dct.values()))