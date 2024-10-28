from sys import stdin
input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
NUMS = sorted(map(int, input().split()))

needs = [False] * (N + 1)
needs[0] = True

for num in NUMS:
    while num <= N:
        if not needs[num]:
            needs[num] = True
            break
        else: num += K

print(int(all(needs)))