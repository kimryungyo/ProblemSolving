N = int(input())
damages = list(map(int, input().split()))
healings = list(map(int, input().split()))

dp = [[0] * (100) for _ in range(N + 1)]
damage = [0] * (N + 1)
heal = [0] * (N + 1)
for i in range(1, N + 1):
    damage[i] = damages[i - 1]
    heal[i] = healings[i - 1]

    for j in range(1, 100):
        if damage[i] <= j:
            dp[i][j] = max(dp[i - 1][j - damage[i]] + heal[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])