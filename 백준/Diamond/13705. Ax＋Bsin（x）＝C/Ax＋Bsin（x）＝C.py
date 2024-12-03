from decimal import Decimal, getcontext

# 각 값의 정확도 설정 (소수점 이하 x자리)
PI_PREC = 128
SIN_PREC = 128
BIN_PREC = 128

# 정확도 적용
ALL_PREC = max(PI_PREC, SIN_PREC, BIN_PREC) + 16
getcontext().prec = ALL_PREC

# 파이값 128자리
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460"[:PI_PREC])



# 테일러 급수를 이용해 sin값을 소수점 이하 약 128자리까지 정확하게 구하는 함수
# x값이 커지면 Decimal에서도 오차가 발생할 수 있기 때문에 주기성을 활용해야 한다
def sin(x: Decimal):
    epsilon = Decimal(f'1e-{SIN_PREC}')
    x %= PI * Decimal("2")

    sin_ = Decimal("0")
    nume = deno = Decimal("1")
    mulx = x
    n = 0
    while True:
        add_ = nume * mulx / deno
        sin_ += add_
        if abs(add_) < epsilon: break
        
        nume *= -1
        deno *= (n + 2) * (n + 3)
        mulx *= x * x
        n += 2

    return sin_



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
