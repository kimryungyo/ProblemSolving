from math import factorial

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p, prime in enumerate(is_prime) if prime]
    return primes

primes = sieve_of_eratosthenes(int(1e9 ** 0.5) + 1)

def prime_factors(n):
    if n <= 1:
        return {}
    
    limit = int(n ** 0.5) + 1
    factors = {}
    
    for prime in primes:
        if prime > limit: break
        while n % prime == 0:
            if prime not in factors:
                factors[prime] = 0
            factors[prime] += 1
            n //= prime
        if n == 1:
            break
    
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    
    return factors

def count_ways(a, b):
    if b == 0: return 1 if a == 0 else 0
    if a < 0: return 0
    
    numerator = factorial(a + b - 1)
    denominator = factorial(b - 1) * factorial(a)
    
    return numerator // denominator

n = int(input())
nums = list(map(int, input().split()))

factors = {}
for num in nums:
    for prime, expo in prime_factors(num).items():
        if prime not in factors:
            factors[prime] = 0
        factors[prime] += expo

count = 1
for factor, expo in factors.items():
    count *= count_ways(expo, n)

print(count % 1000000009)