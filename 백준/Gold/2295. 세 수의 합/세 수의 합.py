from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

nums_set = set(nums)

max_d = -1
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            sum_ = nums[i] + nums[j] + nums[k]
            if sum_ in nums_set:
                if sum_ > max_d:
                    max_d = sum_

print(max_d)