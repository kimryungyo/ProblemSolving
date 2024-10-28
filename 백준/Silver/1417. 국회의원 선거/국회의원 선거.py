N, me, *nums = map(int, open(0))
if N == 1: print(0); quit()

count = 0
while me <= (max_vote := max(nums)):
    nums[nums.index(max_vote)] -= 1
    me += 1
    count += 1

print(count)