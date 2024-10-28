def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i] == True:
            for j in range(i * i, n + 1, i):
                numbers[j] = False
    
    primes = [num for num in range(2, n + 1) if numbers[num] == True]
    return primes

primes = eratosthenes_sieve(1000000)
primes_set = set(primes)

n = int(input())
if n < 8: print(-1); quit()

if n % 2 == 0: 
    a, b = 2, 2
    n -= 4
else: 
    a, b = 2, 3
    n -= 5

for i in range(len(primes)):
    c = primes[i]
    if c > n: break

    for j in range(i, len(primes)):
        d = primes[j]
        if c + d > n: break

        if c + d == n:
            print(a, b, c, d)
            quit()

print(-1)