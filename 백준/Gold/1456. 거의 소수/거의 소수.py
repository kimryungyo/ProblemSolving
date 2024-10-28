# 에라토스테네스의 체 알고리즘 구현
def eratosthenes_sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p**2 <= n:
        if prime[p] == True:
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    result = [p for p in range(2, n) if prime[p]]
    return result


a, b = map(int, input().split())

primes = eratosthenes_sieve(int(b ** 0.5) + 1)

count = 0

for prime in primes:
    num = prime

    for i in range(1, int(1e100)):
        num *= prime
        if a <= num <= b: count += 1
        elif num > b: break

print(count)    