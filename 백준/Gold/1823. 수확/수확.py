from sys import stdin
input = stdin.readline

N = int(input())
values = [int(input()) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = values[i] * N

for length in range(2, N + 1):
    harvest_order = N - length + 1
    for i in range(N - length + 1):
        j = i + length - 1
        left_pick = values[i] * harvest_order + dp[i + 1][j]
        right_pick = values[j] * harvest_order + dp[i][j - 1]
        dp[i][j] = max(left_pick, right_pick)

print(dp[0][N - 1])