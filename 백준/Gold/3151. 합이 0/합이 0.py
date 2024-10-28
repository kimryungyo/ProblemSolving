from collections import Counter
n = int(input())
nums = sorted(map(int, input().split()))
numbers = dict(Counter(nums))

count = 0
for i in range(len(nums) - 2):
    num_a = nums[i]
    numbers[num_a] -= 1

    cans = numbers.copy()
    for j in range(i + 1, len(nums) - 1):
        num_b = nums[j]
        cans[num_b] -= 1

        target = (num_a + num_b) * -1
        if target in cans:
            count += cans[target]

print(count)