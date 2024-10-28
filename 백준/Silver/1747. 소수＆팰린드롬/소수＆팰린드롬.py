from bisect import bisect_left
from sys import stdin
input = lambda: stdin.readline().rstrip()

def eratosthenes_sieve(n):
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
    
    return [i for i in range(2, n+1) if prime_list[i]]

primes = eratosthenes_sieve(1003001)

def is_palindrome(num):
    return str(num) == str(num)[::-1]

N = int(input())
idx = bisect_left(primes, N)

while True:
    prime = primes[idx]

    if is_palindrome(prime):
        print(prime)
        quit()

    idx += 1