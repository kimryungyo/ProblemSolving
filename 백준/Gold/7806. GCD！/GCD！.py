from sys import stdin
input = lambda: stdin.readline().rstrip()

def prime_factors(n):
    factors = {}
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            if i in factors: factors[i] += 1
            else: factors[i] = 1
            n //= i
    if n != 1: factors[n] = 1
    return factors

def count_n_in_factorial(f, n):
    count = 0

    modular = n
    while modular <= f:
        count += f // modular
        modular *= n

    return count

while True:
    try:
        n, k = map(int, input().split())
        k_factors = prime_factors(k)

        gcd = 1
        for factor, k_power in k_factors.items():
            n_power = count_n_in_factorial(n, factor)
            gcd *= factor ** min(n_power, k_power)

        print(gcd)

    except: break