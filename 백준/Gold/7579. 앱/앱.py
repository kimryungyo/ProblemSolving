from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

max_total_c = sum(c)
dp = [0] * (max_total_c + 1)

for i in range(N):
    ci = c[i]
    mi = m[i]
    for current_c in range(max_total_c, ci -1, -1):
        if dp[current_c - ci] + mi > dp[current_c]:
            dp[current_c] = dp[current_c - ci] + mi

for c_sum in range(max_total_c +1):
    if dp[c_sum] >= M:
        print(c_sum)
        break