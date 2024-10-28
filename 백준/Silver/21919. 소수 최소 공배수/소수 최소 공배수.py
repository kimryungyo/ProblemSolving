from math import lcm

def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = { num for num in range(2, n + 1) if numbers[num] }
    return primes

primes = eratosthenes_sieve(1000000)

n, *nums = map(int, open(0).read().split())
prime_nums = set(nums) & primes
print( lcm(*prime_nums) if prime_nums else -1 )