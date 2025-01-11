from sys import stdin
input = stdin.readline

MOD = 998244353

N, K = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N) ]
table = [ [ { 0: 0 } for _ in range(N) ] for _ in range(N) ]
table[0][0][grid[0][0] % K] = 1

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue

        value = grid[i][j]
        if value == -1: 
            continue

        if i > 0:
            for k, v in table[i - 1][j].items():
                new_value = (k * value) % K

                if new_value not in table[i][j]:
                    table[i][j][new_value] = 0

                table[i][j][new_value] += v

        if j > 0:
            for k, v in table[i][j - 1].items():
                new_value = (k * value) % K

                if new_value not in table[i][j]:
                    table[i][j][new_value] = 0

                table[i][j][new_value] += v

        for k, v in table[i][j].items():
            table[i][j][k] = v % MOD

answer = table[i][j][0]
print(answer)