def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:
                divisors.append(i)

            if i != 1 and i != n // i and n // i != n:
                divisors.append(n // i)

    return sorted(divisors)

def check_perfect_number(n):
    divisors = get_divisors(n)
    sum_divisors = sum(divisors)

    if sum_divisors == n:
        return f"{n} = " + " + ".join(map(str, divisors))

    else:
        return f"{n} is NOT perfect."
    
import sys
input = sys.stdin.read
data = input().strip().split()

results = []
for num in data:
    n = int(num)
    if n == -1:
        break
    results.append(check_perfect_number(n))

for result in results:
    print(result)