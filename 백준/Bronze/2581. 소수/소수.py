M = int(input())
N = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = 0
min_prime = -1

for i in range(M, N+1):
    if is_prime(i):
        prime_sum += i
        if min_prime == -1 or i < min_prime:
            min_prime = i

if min_prime == -1:
    print(-1)
else:
    print(prime_sum)
    print(min_prime)