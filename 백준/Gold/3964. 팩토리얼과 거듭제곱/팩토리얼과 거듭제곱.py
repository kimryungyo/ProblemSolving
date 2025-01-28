from sys import stdin
input = stdin.readline

def factorize(n):
    factors = {}
    
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
        
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 2
        
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def v_p_of_factorial(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    
    factor_dict = factorize(k)

    answer = float('inf')
    for p, exp in factor_dict.items():
        vp = v_p_of_factorial(n, p)
        answer = min(answer, vp // exp)

    print(answer)