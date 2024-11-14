N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):

    is_prime = True
    if numbers[i] == 1:
        is_prime = False
        
    for j in range(2, int(numbers[i] ** 0.5) + 1):
        if numbers[i] % j == 0:
            is_prime = False
            break

    if is_prime: count += 1

print(count)