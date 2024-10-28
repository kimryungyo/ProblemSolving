from math import comb
n = int(input())

def get_combinations(x):
    a = 52 - x * 4
    b = n - x * 4
    combs = comb(a, b)
    return combs

sign = 1
count = 0
for stack in range(1, n // 4 + 1):
    multiply = comb(13, stack)
    combs = get_combinations(stack)
    count += combs * multiply * sign
    sign *= -1

print(count % 10007)