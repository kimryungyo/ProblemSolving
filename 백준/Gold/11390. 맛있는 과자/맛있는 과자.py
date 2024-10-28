from math import log, comb
from fractions import Fraction

a, b, n, k = map(int, input().split())
cp2 = Fraction(a ** 2 + b ** 2)

root_area = Fraction(a * b, 2)
min_ratio, max_ratio = sorted([Fraction(a ** 2, cp2), Fraction(b ** 2, cp2)])

index = 0
for i in range(n + 1):
    count = comb(n, i)
    index += count

    if index >= k:
        ratio = (min_ratio ** i) * (max_ratio ** (n - i))
        area = root_area * ratio
        log_area = log(area)
        print(log_area)
        quit()