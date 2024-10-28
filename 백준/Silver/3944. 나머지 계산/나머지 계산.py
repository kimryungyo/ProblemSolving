from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    B, D = input().split()
    sum_ = 0
    for num in D: sum_ += int(num)
    print(sum_ % (int(B) - 1))