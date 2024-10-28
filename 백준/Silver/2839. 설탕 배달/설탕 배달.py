from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
min_count = -1

for big in range(n // 5 + 1):
    remain = n - big * 5
    if remain % 3 == 0:
        small = remain // 3
        min_count = big + small

print(min_count)