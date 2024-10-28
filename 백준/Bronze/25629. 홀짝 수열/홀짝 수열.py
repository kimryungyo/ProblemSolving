from sys import stdin
input = lambda: stdin.readline()

n = int(input())
nums = map(int, input().split())

odd = sum(1 for i in nums if i % 2 == 1)
even = n - odd

print(1 if odd == int(n / 2 + 0.5) and even == n // 2 else 0)