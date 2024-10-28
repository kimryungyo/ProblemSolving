from collections import Counter

n = int(input())
nums = sorted(map(int, input().split()))
count = 0

cases = []

# case 1
case1_nums = nums.copy()
case1_craft = case1_nums.pop()
cases.append((case1_nums, case1_craft))

# case 2
case2_nums = nums.copy()
case2_craft = case2_nums.pop(-2)
cases.append((case2_nums, case2_craft))

# case 3
case3_nums = nums.copy()
case3_nums.pop()
case3_nums.pop()
case3_craft =  case3_nums.pop()
if sum(case3_nums) == case3_craft:
    count += 1

for nums, craft in cases:

    num_counts = dict(Counter(nums))
    total = sum(nums)

    for num in nums:
        target = (total - craft) - num
        num_counts[num] -= 1
        
        if target in num_counts:
            count += num_counts[target]

print(count)