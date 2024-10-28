from math import gcd
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    max_gcd = 0
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):

            gcd_ = gcd(nums[i], nums[j])

            if gcd_ > max_gcd:
                max_gcd = gcd_

    print(max_gcd)