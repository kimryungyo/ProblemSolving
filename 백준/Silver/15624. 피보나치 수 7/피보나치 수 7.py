n = int(input())
MOD = 10 ** 9 + 7

if n == 0: print(0)
elif n == 1: print(1)
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    print(b)