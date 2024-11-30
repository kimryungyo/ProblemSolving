from decimal import Decimal, getcontext

# 각 값의 정확도 설정 (소수점 이하 x자리)
PI_PREC = 128
SIN_PREC = 128
BIN_PREC = 128

# Decimal에 정확도 적용
ALL_PREC = max(PI_PREC, SIN_PREC, BIN_PREC) + 16
getcontext().prec = ALL_PREC

# 파이값 128자리
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460")



# 테일러 급수를 이용해 sin값을 소수점 이하 약 128자리까지 정확하게 구하는 함수
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



# Ax + Bsin(x) - C 값을 반환하는 함수
def function(x):
    return A * x + B * sin(x) - C



# 오차가 소수점 이하 128자리가 될 때 까지 이분 탐색을 하는 함수
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


# Ax + Bsin(x) = C 을 만족하는 x값을 반올림해 소수점 여섯째까지 출력하는 코드 
A, B, C = map(int, input().split())
result = binary_search()
print(f"{round(result, 6):.6f}")
