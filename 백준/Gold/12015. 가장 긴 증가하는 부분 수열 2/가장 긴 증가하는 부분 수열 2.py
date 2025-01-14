import bisect

N = int(input())
nums = list(map(int, input().split()))

dp = []
for num in nums:
    idx = bisect.bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num
        
print(len(dp))