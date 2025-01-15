from math import log, floor

N = int(input())
MOD = 2 ** 32

def eratosthenes_bit(n):
    if n < 2: return []
    
    sieve_size = (n // 2) + 1
    sieve = bytearray((sieve_size + 7) // 8)
    sieve[:] = b'\xFF' * len(sieve)
    
    sieve[0] &= ~0x01

    limit = int(floor((n ** 0.5 - 1) / 2)) + 1
    for i in range(1, limit):
        byte_index = i // 8
        bit_index = i % 8

        if sieve[byte_index] & (1 << bit_index):
            p = 2 * i + 1
            start = (p * p - 1) // 2

            for multiple in range(start, sieve_size, p):
                sieve[multiple // 8] &= ~(1 << (multiple % 8))
    
    primes = [2] + [2 * i + 1 for i in range(1, sieve_size) if sieve[i // 8] & (1 << (i % 8))]
    return primes

primes = eratosthenes_bit(N)

lcm = 1
for prime in primes:
    power = int(log(N, prime))
    lcm *= pow(prime, power)
    lcm %= MOD

print(int(lcm))