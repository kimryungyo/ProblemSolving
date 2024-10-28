counts = [0] * 100001
*nums, S = map(int, open(0).read().split())
for num in nums: counts[num] += 1

checked = set()

result = 0
for num in sorted(nums):
    counts[num] -= 1
    other = S - num
    
    if 0 <= other <= 100000 and counts[other] and (num, other) not in checked:
        checked.add((num, other))
        result += 1
        print(num, other)

print(result) 