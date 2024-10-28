from sys import stdin
input = lambda: stdin.readline().rstrip()

len = int(input())
s = input().split()

dp = [2000 for _ in range(len + 1)]
dp[-1] = 0
is_p = [[0 for j in range(len)] for i in range(len)]

for i in range(len): is_p[i][i] = 1

for i in range(1, len):
    if s[i - 1] == s[i]:
        is_p[i - 1][i] = 1

for l in range(3, len + 1):
    for start in range(len - l + 1):
        end = start + l - 1
        if s[start] == s[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = 1

q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    print(1 if is_p[s-1][e-1] else 0)