from math import gcd

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    sum_ = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            gcd_ = gcd(nums[i], nums[j])
            sum_ += gcd_

    print(sum_)