MOD = 10 ** 9 + 7

def find_modular_inverse(modulus, number):
    ret = 1
    while number:
        if number & 1:
            ret = ret * modulus % MOD
        modulus = modulus * modulus % MOD
        number >>= 1
    return ret

k, n = map(int, input().split())
a, b = 1, 1

for i in range(k + 1):
    a = a * (k + n - i) % MOD
    b = b * (k + 1 - i) % MOD

print(a * find_modular_inverse(b, MOD - 2) % MOD)