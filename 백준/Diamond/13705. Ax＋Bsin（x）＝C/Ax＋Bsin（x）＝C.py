from decimal import Decimal, getcontext

PI_PREC = 128
SIN_PREC = 64
BIN_PREC = 64

ALL_PREC = max(SIN_PREC, BIN_PREC) + 16
getcontext().prec = ALL_PREC

PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460")

def sin(x):
    epsilon = Decimal(f'1e-{SIN_PREC}')
    TWO_PI = 2 * PI

    x = x % TWO_PI

    exp = deno = sign = 1
    result = powers = Decimal(x)
    x_suqare = Decimal(x) ** 2

    while True:
        exp += 2
        deno *= exp * (exp - 1)
        powers *= x_suqare
        sign *= -1
        term = (powers / Decimal(deno)) * sign
        result += term

        if abs(term) < epsilon:
            break

    return result

def function(x):
    return A * x + B * sin(x) - C

def binary_search():
    epsilon = Decimal(f'1e-{BIN_PREC}')

    left, right = Decimal("-0.1"), Decimal("100000.1")
    while right - left > epsilon:
        mid = (left + right) / Decimal("2")
        if function(mid) > Decimal("0"):
            right = mid
        else:
            left = mid

    return left

A, B, C = map(int, input().split())
result = binary_search()
print(f"{round(result, 6):.6f}")