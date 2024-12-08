N, M = map(int, input().split())

if N == 1:
    print(0)
    quit()

def prime_factorization(x):
    factors = {}
    num = x
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors[d] = factors.get(d, 0) + 1
            num //= d
        d += 1 if d == 2 else 2
    if num > 1:
        factors[num] = factors.get(num, 0) + 1
    return factors

def main():
    factors = prime_factorization(M)
    n = N - 1

    factorial_exp = {}
    for p in factors.keys():
        exponent_p_of_i = [0] * (n + 1)

        power = p
        while power <= n:
            for multiple in range(power, n + 1, power):
                exponent_p_of_i[multiple] += 1
            power *= p

        factorial_p_exp_p = [0] * (n + 1)
        for i in range(1, n+1):
            factorial_p_exp_p[i] = factorial_p_exp_p[i-1] + exponent_p_of_i[i]

        factorial_exp[p] = factorial_p_exp_p

    unnecessary = []
    for k in range(0, N):
        divisible = True
        for p, a in factors.items():
            f = factorial_exp[p]
            exp_ck = f[n] - f[k] - f[n-k]
            if exp_ck < a:
                divisible = False
                break

        if divisible:
            unnecessary.append(k + 1)

    print(len(unnecessary))
    if unnecessary:
        print(' '.join(map(str, unnecessary)))
        
main()