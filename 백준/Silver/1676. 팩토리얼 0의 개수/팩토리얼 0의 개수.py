from math import factorial

n = int(input())
value = factorial(n)

count = 0
while value % 10 == 0:
    value //= 10
    count += 1

print(count)