n, *datas = map(int, open(0).read().split())
players = [(datas[i], i) for i in range(n)]
players.sort(key=lambda x: x[0])

dp = [(0, 0)] * (n + 1)         # dp[i] : (팀 수, 총 비용)
decision = [None] * (n + 1)     # decision[i] : 각 선수에 대한 선택, skip or team
dp[n] = (0, 0)

for i in range(n - 1, -1, -1):
    skip = dp[i + 1]
    best = skip
    best_decision = 'skip'
    if i + 3 < n:
        candidate = (1 + dp[i + 4][0], (players[i + 3][0] - players[i][0]) + dp[i + 4][1])
        if (candidate[0], -candidate[1]) > (best[0], -best[1]):
            best = candidate
            best_decision = 'team'
    dp[i] = best
    decision[i] = best_decision

total_cost = dp[0][1]

used = [False] * n
i = 0
while i < n:
    if decision[i] == 'team' and i + 3 < n:
        used[i] = used[i + 1] = used[i + 2] = used[i + 3] = True
        i += 4
    else:
        i += 1

skipped = [players[i][1] for i in range(n) if not used[i]]
skipped.sort()

print(total_cost)
print("\n".join(map(str, skipped)))