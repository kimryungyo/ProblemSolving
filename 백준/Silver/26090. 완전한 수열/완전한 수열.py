def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = { num for num in range(2, n + 1) if numbers[num] }
    return primes

primes = eratosthenes_sieve(500 * 2000)
n, *nums = map(int, open(0).read().split())

count = 0
for i in range(n):
    sum = leng = 0
    for j in range(i, n):
        sum += nums[j]
        leng += 1

        if sum in primes and leng in primes:
            count += 1

print(count)