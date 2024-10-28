n, *nums = map(int, open(0).read().split())
nums.sort()
num = 0

for i in range(n):
    num += nums[i] * 2 * (i * 2 - n + 1)

print(num)