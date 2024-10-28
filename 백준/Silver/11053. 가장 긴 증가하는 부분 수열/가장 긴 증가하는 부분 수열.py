from sys import stdin
input = lambda: stdin.readline().rstrip()

n, *nums = map(int, open(0).read().split())

dp = [ 1 ] * n
max_length = 1

for i in range(n):
    num = nums[i]

    for j in range(i):
        sub_num = nums[j]

        if num > sub_num:
            length = dp[j] + 1
            
            if length > dp[i]:
                dp[i] = length
                max_length = max(max_length, length)

print(max_length)