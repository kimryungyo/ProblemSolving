from collections import Counter
n, *nums = map(int, open(0).read().split())
nums.sort()

counts = []
for num, count in dict(Counter(nums)).items():
    counts.append( (count, -num) )
counts.sort(reverse=True)

max_count = counts[0][0]
mode = -counts[0][1]
if len(counts) > 1 and counts[1][0] == max_count: 
    mode = -counts[1][1]

average = round(sum(nums) / n)
median = nums[n // 2]
range = nums[-1] - nums[0]

print(average)
print(median)
print(mode)
print(range)