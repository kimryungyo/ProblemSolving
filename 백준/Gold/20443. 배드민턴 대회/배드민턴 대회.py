from math import comb

MOD = 10 ** 9 + 7
N = int(input())

DP = [0] * (N + 1)
DP[2] = 1

for i in range(N - 2): 
    DP[i+3] = ( (i + 2) * (DP[i + 2] + DP[i + 1]) ) % MOD

excluded = N % 4
included = N - excluded

exclude = comb(N, excluded)
permutation = DP[included]

count = exclude * permutation
print(count % MOD)