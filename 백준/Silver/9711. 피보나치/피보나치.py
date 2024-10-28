from sys import stdin
input = lambda: stdin.readline().rstrip()

fibo = [0, 1] + [0] * (10000 - 1)
for i in range(2, 10000 + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

T = int(input())
for num in range(1, T + 1):
    P, Q = map(int, input().split())
    result = fibo[P] % Q
    print(f"Case #{num}: {result}")