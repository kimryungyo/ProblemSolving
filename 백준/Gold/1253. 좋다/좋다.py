n = int(input())
nums = list(map(int, input().split()))
goods = set()

num_idxs = {}
for i in range(len(nums)):
    num = nums[i]
    if num not in num_idxs:
        num_idxs[num] = set()
    num_idxs[num].add(i)

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        sum_ = nums[i] + nums[j]
        if sum_ in num_idxs:
            new_goods = set()
            for idx in num_idxs[sum_]:
                if idx != i and idx != j:
                    new_goods.add(idx)
            num_idxs[sum_] -= new_goods
            goods |= new_goods
                        
print(len(goods))