MOD = 10 ** 9 + 7
N, R = map(int, input().split())

facts = [1]
for i in range(1, N + 1):
    new = facts[-1] * i % MOD
    facts.append(new)

comb = facts[N]

comb *= pow(facts[N-R], MOD - 2, MOD)
comb %= MOD

comb *= pow(facts[R], MOD - 2, MOD)
comb %= MOD

print(comb)