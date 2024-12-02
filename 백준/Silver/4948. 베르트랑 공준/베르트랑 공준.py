from sys import stdin
input = stdin.readline

def sieve(max_limit):
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False
    for current in range(2, int(max_limit ** 0.5) + 1):
        if is_prime[current]:
            for multiple in range(current * current, max_limit + 1, current):
                is_prime[multiple] = False
    return is_prime

test_cases = []
while True:
    line = input()
    if not line: break
    n = int(line.strip())
    if n == 0: break
    test_cases.append(n)

if test_cases:
    max_n = max(test_cases)
    sieve_limit = 2 * max_n
    is_prime = sieve(sieve_limit)

    prime_count = [0] * (sieve_limit + 1)
    count = 0
    for number in range(1, sieve_limit + 1):
        if is_prime[number]:
            count += 1
        prime_count[number] = count

    for n in test_cases:
        primes_between = prime_count[2 * n] - prime_count[n]
        print(primes_between)