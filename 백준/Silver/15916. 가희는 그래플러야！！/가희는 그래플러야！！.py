n, *nums, k = map(int, open(0).read().split())

if nums[0] == k: print("T"); quit()
bef_pos = nums[0] > k

for x in range(1, n):
    linear = k * (x + 1)
    function = nums[x]
    if linear == function: print("T"); quit()
    pos = function > linear
    if pos != bef_pos: print("T"); quit()

print("F")