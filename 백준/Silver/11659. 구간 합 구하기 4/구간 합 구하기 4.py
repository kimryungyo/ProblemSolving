from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + numbers[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
