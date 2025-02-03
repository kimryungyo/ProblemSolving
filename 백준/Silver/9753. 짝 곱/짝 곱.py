from bisect import bisect_left
from sys import stdin
input = lambda: stdin.readline().rstrip()

def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = [ num for num in range(2, n + 1) if numbers[num] ]
    return primes

primes = eratosthenes_sieve(100000)
products = [100001]

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        multiply = primes[i] * primes[j]
        if multiply > 100000: break
        products.append(multiply)

products.sort()

T = int(input())
for _ in range(T):
    K = int(input())
    print(products[bisect_left(products, K)])