N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 1

for num in numbers:
    result = (result * num) % M

print(result)