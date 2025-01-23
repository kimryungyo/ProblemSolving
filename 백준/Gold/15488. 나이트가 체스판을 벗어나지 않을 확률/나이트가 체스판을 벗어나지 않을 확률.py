N, x, y, K = map(int, input().split())

moves = [(1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

curr_dp = [[0.0] * (N+1) for _ in range(N+1)]
next_dp = [[0.0] * (N+1) for _ in range(N+1)]

curr_dp[x][y] = 1.0

for _ in range(K):
    for i in range(1, N+1):
        for j in range(1, N+1):
            next_dp[i][j] = 0.0
    
    for r in range(1, N+1):
        for c in range(1, N+1):
            prob = curr_dp[r][c]
            if prob > 0:
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= N and 1 <= nc <= N:
                        next_dp[nr][nc] += prob / 8.0
    
    curr_dp, next_dp = next_dp, curr_dp

answer = sum(sum(row) for row in curr_dp)

print(f"{answer:.9f}")