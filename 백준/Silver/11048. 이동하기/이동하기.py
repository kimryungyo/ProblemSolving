import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = candies[0][0]

for c in range(1, M):
    dp[0][c] = dp[0][c-1] + candies[0][c]

for r in range(1, N):
    dp[r][0] = dp[r-1][0] + candies[r][0]

for r in range(1, N):
    for c in range(1, M):
        dp[r][c] = candies[r][c] + max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

print(dp[N-1][M-1])