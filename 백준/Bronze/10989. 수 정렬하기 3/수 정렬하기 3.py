from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
nums = {}

for _ in range(n):
    num = int(input())
    if num not in nums: nums[num] = 0
    nums[num] += 1

for num in sorted(nums.keys()):
    for _ in range(nums[num]):
        print(num)