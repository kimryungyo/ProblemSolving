mod = 1000000000

def matrix_mult(x, y):
    return [[(x[0][0] * y[0][0] + x[0][1] * y[1][0]) % mod, (x[0][0] * y[0][1] + x[0][1] * y[1][1]) % mod],
            [(x[1][0] * y[0][0] + x[1][1] * y[1][0]) % mod, (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % mod]]

def matrix_pow(mat, power):
    result = [[1, 0], [0, 1]]
    base = mat
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    f = [[1, 1], [1, 0]]
    f_n = matrix_pow(f, n-1)
    return f_n[0][0]

def fibonacci_sum(n):
    if n == 0:
        return 0
    return (fibonacci(n + 2) - 1 + mod) % mod

def range_fibonacci_sum(a, b):
    if a > b:
        return 0
    sum_b = fibonacci_sum(b)
    sum_a_minus_1 = fibonacci_sum(a - 1)
    return (sum_b - sum_a_minus_1 + mod) % mod

a, b = map(int, input().split())

result = range_fibonacci_sum(a, b)

print(result)