MOD = 1000000
N = int(input())
if N == 1: print(1); quit()

prev = [1]

for step in range(1, N):
    curr = [0] * (step + 1)

    for k in range(1, step + 1):
        curr[k] = (curr[k - 1] + prev[step - k]) % MOD

    prev = curr

one_side = sum(prev) % MOD
print( (2 * one_side) % MOD )