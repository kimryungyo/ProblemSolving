import sys
sys.setrecursionlimit(25600)

n = int(input())
nums = sorted(map(int, input().split()))

def power(a, b):
    if b == 0: return 1
    x = power(a, b//2)
    x %= 1000000007
    if b % 2 == 0: return x * x
    else: return x * x * a

count = 0
for i in range(n):
    num = nums[i]
    min_count = power(2, n - i - 1)
    max_count = power(2, i)
    count += (max_count - min_count) * num

print(count % 1000000007)