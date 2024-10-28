from fractions import Fraction
A = Fraction(*map(int, input().split()))
B = Fraction(*map(int, input().split()))
C = A + B
print(C.numerator, C.denominator)