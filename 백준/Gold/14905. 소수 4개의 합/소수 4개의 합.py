def is_prime(n):
    k = 2
    if n < 2: return False
    while k ** 2 <= n:
        if n % k == 0: return False
        k += 1
    return True

queries = list(map(int, open(0).read().split()))
for n in queries:

    if n < 8: print("Impossible."); continue

    if n % 2 == 0: 
        a, b = 2, 2
        n -= 4
    else: 
        a, b = 2, 3
        n -= 5

    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            c, d = i, n - i
            print(a, b, c, d)
            break