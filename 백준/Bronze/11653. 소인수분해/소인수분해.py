n = int(input())
prime = 1
while n > 1:
    prime += 1
    while n % prime == 0:
        n //= prime
        print(prime)