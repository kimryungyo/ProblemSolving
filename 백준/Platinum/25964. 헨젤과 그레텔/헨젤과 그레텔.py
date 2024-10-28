MOD = 10**9 + 7
MAX_N = 200000

def mod_inv(x, mod): return pow(x, mod - 2, mod)

def pre_fact_and_inv(max_n, mod):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[max_n] = mod_inv(fact[max_n], mod)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def comb(n, k, fact, inv_factorial, mod):
    if k > n or k < 0: return 0
    return fact[n] * inv_factorial[k] % mod * inv_factorial[n - k] % mod

def perm(n, k, fact, mod):
    if k > n or k < 0: return 0
    return fact[n] * mod_inv(fact[n - k], mod) % mod

fact, inv_fact = pre_fact_and_inv(MAX_N, MOD)

N, K = map(int, input().split())

total = perm(N, K, fact, MOD) * perm(N, K, fact, MOD) % MOD

others = 0
for num in range(1, K + 1):
    comb_K_num = comb(K, num, fact, inv_fact, MOD)
    fact_num = fact[num]
    comb_N_num = comb(N, num, fact, inv_fact, MOD)
    perm_N_num = perm(N - num, K - num, fact, MOD) ** 2 % MOD

    other = comb_K_num * fact_num % MOD * comb_N_num % MOD * perm_N_num % MOD
    if num % 2 == 1:
        others = (others + other) % MOD
    else:
        others = (others - other) % MOD

print((total - others + MOD) % MOD)