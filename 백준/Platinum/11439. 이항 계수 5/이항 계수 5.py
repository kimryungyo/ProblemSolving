N, K, MOD = map(int, input().split())

def eratosthenes_sieve(n):
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
    
    return [i for i in range(2, n+1) if prime_list[i]]

def factorial(n):
    numbers = [0] * (N + 1)

    for prime in primes:
        if prime > n: break
        modular = prime
        while modular <= n:
            numbers[prime] += n // modular
            modular *= prime

    return numbers

primes = eratosthenes_sieve(N)
numbers = [0] * (N + 1)

for num, power in enumerate(factorial(N)):
    numbers[num] += power

for num, power in enumerate(factorial(N - K)):
    numbers[num] -= power

for num, power in enumerate(factorial(K)):
    numbers[num] -= power

result = 1
for number in range(1, N + 1):
    if numbers[number]:
        result *= pow(number, numbers[number], MOD)
        result %= MOD

print(result)