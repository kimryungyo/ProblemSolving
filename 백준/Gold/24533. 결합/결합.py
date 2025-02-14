from sys import stdin
input = stdin.readline

N = int(input().strip())
sum_a = sum_b = sum_ab = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum_a += a
    sum_b += b
    sum_ab += a * b

print(sum_a * sum_b - sum_ab)