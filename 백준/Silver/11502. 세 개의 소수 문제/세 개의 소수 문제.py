from sys import stdin
input = lambda: stdin.readline().rstrip()

def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = [num for num in range(2, n + 1) if numbers[num]]
    return primes

primes = eratosthenes_sieve(1000)
primes_set = set(primes)

T = int(input())
for _ in range(T):
    K = int(input())
    end = False

    for a in primes:
        if a >= K: continue

        for b in primes:
            if a + b >= K: continue

            target = K - (a + b)

            if target in primes_set:
                print(a, b, target)
                end = True; break

        if end: break