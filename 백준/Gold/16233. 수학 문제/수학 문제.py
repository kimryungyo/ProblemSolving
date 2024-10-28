from sys import stdin
input = lambda: stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 9 != 0: print(-1, end = " "); continue
    
    r = 999999999
    x = 0
    while r:
        if 9 < (n // r): break
        x = (x + n // r) * 10
        n %= r
        r //= 10

    if r != 0: print(-1, end = " ")
    else: print(x, end=' ')