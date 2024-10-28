n, *nums = map(int, open(0).read().split())
order = sorted(set(nums))
idxs = { v: i for i, v in enumerate(order) }
for num in nums:
    print(idxs[num], end = " ")