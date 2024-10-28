MOD = 10 ** 9 + 7
N, K = map(int, input().split())

facts = [1]

num = 1
for i in range(1, N + 1):
    num *= i
    num %= MOD
    facts.append(num)
    
def get_mod_inv(num): return pow(num, MOD - 2, MOD)

upper = facts[N]
lower = facts[N - K] * facts[K]
mod_inv = get_mod_inv(lower)

binomial = ( (upper % MOD) * (mod_inv % MOD) ) % MOD
print(binomial)