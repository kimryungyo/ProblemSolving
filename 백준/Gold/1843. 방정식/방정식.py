n = int(input())

# case 1
# X Y Z = N 이하이며 모두 다름
count = 0
for x in range(1, (n+1)//2):
    count += (n - x) - x
print(count)


# case 2
# X Y Z = N의 양의 약수

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    return divisors

divisors = find_divisors(n)
divisors_set = set(divisors)

count = 0
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        if divisors[i] + divisors[j] in divisors_set:
            count += 1

print(count)


# case 3
# X Y Z = N 이하의 양의 소수

def eratosthenes_sieve(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = [num for num in range(2, n + 1) if numbers[num]]
    return primes

primes = eratosthenes_sieve(n)
primes_set = set(primes)

count = 0

for prime in primes:
    if 2 + prime in primes_set:
        count += 1

print(count)