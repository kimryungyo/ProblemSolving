n, k = map(int, input().split())
nums = list(map(int, input().split()))

sums = {0: 1}
sum_ = 0
count = 0
for num in nums:
    sum_ += num
    target = (k - sum_) * -1
    if target in sums:
        count += sums[target]

    if sum_ not in sums:
        sums[sum_] = 0
    sums[sum_] += 1
    
print(count)
