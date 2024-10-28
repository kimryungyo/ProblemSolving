def eratosthenes_sieve(n):
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
    
    primes = [i for i in range(2, n+1) if prime_list[i]]
    return primes

primes = eratosthenes_sieve(100000)
primes_set = set(primes)

def is_prime_factor_length(num):
    leng = 0
    for prime in primes:
        if prime > num: break
        while num % prime == 0:
            leng += 1
            num //= prime
        if num == 1: break
    if leng in primes_set: return True
    else: return False

A, B = map(int, input().split())
count = 0
for i in range(A, B + 1):
    if is_prime_factor_length(i):
        count += 1
print(count)