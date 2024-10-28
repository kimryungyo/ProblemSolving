def find_primes(n: int) -> list:
    primes = [True] * (n+1)
    
    for i in range(2, (n // 2) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]]

def find_and_print_primes():
    min_val, max_val = map(int, input().split())
    primes = find_primes(max_val)

    for prime in primes:
        if prime >= min_val: print(prime)

find_and_print_primes()
