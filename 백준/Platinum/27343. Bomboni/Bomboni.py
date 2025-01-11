from sys import stdin
input = stdin.readline

def factorize(n):
    factors = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors: factors[i] = 0
            factors[i] += 1
    if n > 1:
        if n not in factors: factors[n] = 0
        factors[n] += 1

    return factors

MOD = 998244353

N, K = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N) ]

k_factors = factorize(K)
need_factors = list(k_factors.keys())

factors_table = [ [ { factor : 0 for factor in need_factors } for _ in range(N) ] for _ in range(N) ]

for i in range(N):
    for j in range(N):

        value = grid[i][j]
        for factor in need_factors:
            while value % factor == 0:
                value //= factor
                factors_table[i][j][factor] += 1
                if factors_table[i][j][factor] >= k_factors[factor]:
                    factors_table[i][j][factor] = "satisfy"
                    break


dict_to_tuple = lambda dic: tuple(sorted(dic.items()))
tuple_to_dict = lambda tup: { k: v for k, v in tup }


dp_table = [ [ {} for _ in range(N) ] for _ in range(N) ]
dp_table[0][0][dict_to_tuple(factors_table[0][0])] = 1

def update_table(k, v):
    before_factors = tuple_to_dict(k)
    new_factors = {}
    for factor in need_factors:
        bef_count = before_factors[factor]
        now_count = factors[factor]

        if bef_count == "satisfy" or now_count == "satisfy":
            new_count = "satisfy"
        else:
            new_count = bef_count + now_count
            if new_count >= k_factors[factor]:
                new_count = "satisfy"

        new_factors[factor] = new_count

    tuple_factors = dict_to_tuple(new_factors)
    if tuple_factors not in dp_table[i][j]:
        dp_table[i][j][tuple_factors] = 0

    dp_table[i][j][tuple_factors] += v

for i in range(N):
    for j in range(N):

        if i == 0 and j == 0: continue
        if grid[i][j] == -1: continue

        factors = factors_table[i][j]

        if i > 0:
            for k, v in dp_table[i - 1][j].items():
                update_table(k, v)

        if j > 0:
            for k, v in dp_table[i][j - 1].items():
                update_table(k, v)

        for k, v in dp_table[i][j].items():
            dp_table[i][j][k] = v % MOD

goal = dict_to_tuple({ factor: "satisfy" for factor in need_factors })
answer = dp_table[N-1][N-1].get(goal, 0)
print(answer)