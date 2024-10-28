def get_mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        if m == 0: return -1
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    if a == 1: return x1 % m0

N, A = map(int, input().split())
add_inverse = N - A
mod_inverse = get_mod_inverse(A, N)
print(add_inverse, mod_inverse)
