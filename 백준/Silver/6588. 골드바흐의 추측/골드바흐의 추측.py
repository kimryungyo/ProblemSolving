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

primes = eratosthenes_sieve(1000000)
primes_set = set(primes)

while True:
    n = int(input())
    if n == 0: break

    for prime in primes:
        remain = n - prime
        if remain in primes_set:
            print(f"{n} = {prime} + {remain}")
            break