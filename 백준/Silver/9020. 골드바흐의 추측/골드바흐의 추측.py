def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_partition(n):
    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            return i, n - i

T = int(input())

for _ in range(T):
    n = int(input())
    result = goldbach_partition(n)
    print(result[0], result[1])
