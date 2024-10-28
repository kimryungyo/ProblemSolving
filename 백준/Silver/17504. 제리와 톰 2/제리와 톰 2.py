from fractions import Fraction
N = int(input())
nums = list(map(int, input().split()))

fraction = Fraction(1, nums.pop())
while nums:
    num = nums.pop()
    fraction = Fraction(1, num + fraction)

fraction = 1 - fraction
nume, deno = fraction.numerator, fraction.denominator
print(nume, deno)