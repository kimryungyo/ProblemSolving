p = int(input())
arr = list(map(int, input().split()))

sums = sum(arr)

a, b = map(int, input().split())

q = (b - a) // p
b -= q * p
result = q * sums

if a < 0:
    q = (-a + p - 1) // p
    a += q * p
    b += q * p

for i in range(a, b):
    result += arr[i % p]

print(result)
