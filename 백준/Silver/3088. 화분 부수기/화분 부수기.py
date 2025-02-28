import sys
input = sys.stdin.readline

N = int(input().strip())
broken_set = set()
direct_breaks = 0

for _ in range(N):
    nums = list(map(int, input().split()))
    if not any(num in broken_set for num in nums):
        direct_breaks += 1
    broken_set.update(nums)

print(direct_breaks)