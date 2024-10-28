MOD = 10 ** 9
N = int(input())
if N == 1: print(0); quit()

DP = [0] * (N + 1)
DP[2] = 1

for i in range(N-2): 
    DP[i+3] = ((i+2) * (DP[i+2]+DP[i+1])) % MOD

print(DP[N])