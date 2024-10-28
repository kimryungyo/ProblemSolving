from math import factorial
from sys import set_int_max_str_digits
set_int_max_str_digits(1000000)
N = int(input())
print(factorial(N))