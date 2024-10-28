from sys import stdin
input = lambda: stdin.readline().rstrip()

MOD = 10 ** 9 + 7
MAX_N = 4000000

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

def comb(n, k):
    if k > n or k < 0: return 0
    return facts[n] * inv_facts[k] % MOD * inv_facts[n - k] % MOD

facts, inv_facts = pre_fact_and_inv(MAX_N, MOD)

M = int(input())
for _ in range(M):
    N, K = map(int, input().split())
    print(comb(N, K) % MOD)