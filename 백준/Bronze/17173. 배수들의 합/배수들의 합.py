N, M = map(int, input().split())

K = list(map(int, input().split()))
sum_multiples = 0

for num in range(1, N + 1):
    for k in K:
        if num % k == 0:
            sum_multiples += num
            break

print(sum_multiples)