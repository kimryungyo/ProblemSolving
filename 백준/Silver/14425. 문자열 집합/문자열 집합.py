from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
S = { input() for _ in range(N) }
count = 0
for _ in range(M):
    if input() in S: count += 1
print(count)