from collections import deque
queue = deque([ (1, set()) ])

def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = [num for num in range(2, n + 1) if numbers[num]]
    return primes

primes = eratosthenes_sieve(100000)
prime_factors = {1: set()}

count = 0
while queue:
    num, factors = queue.popleft()
    
    for prime in primes:
        next = num * prime
        if next > 100000: break
        if next in prime_factors: continue

        if prime not in factors: next_fac = factors | {prime}
        else: next_fac = factors
        
        queue.append((next, next_fac))
        prime_factors[next] = next_fac

n, *nums = map(int, open(0).read().split())
nums.sort()

count = 0
bef_num, bef_fac = None, set()
for num in nums:
    factors = prime_factors[num]

    if factors & bef_fac:
        only_one = False
        for i in range(bef_num, num + 1):
            if not ((bef_fac & prime_factors[i]) or (factors & prime_factors[i])):
                only_one = True
                break
        if only_one: count += 1
        else: count += 2

    bef_num, bef_fac = num, factors

print(count)