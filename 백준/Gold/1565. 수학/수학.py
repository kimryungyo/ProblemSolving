from math import lcm

ds, ms = map(int, input().split())
d = list(map(int, input().split()))
m = sorted(map(int, input().split()))

d_gcd = lcm(*d)
min_m = m[0]

divisors = set()
for i in range(1, int(min_m ** (1 / 2)) + 1):
    if (min_m % i == 0):
        new_div = i
        if new_div % d_gcd == 0:
            divisors.add(new_div)

        if ( (i ** 2) != min_m) : 
            new_div = min_m // i
            if new_div % d_gcd == 0:
                divisors.add(new_div)

for num in m:
    removes = set()
    for div in divisors:
        if num % div != 0:
            removes.add(div)
    divisors -= removes
print(len(divisors))