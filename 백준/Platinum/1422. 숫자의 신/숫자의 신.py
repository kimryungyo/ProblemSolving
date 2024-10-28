from sys import stdin
input = lambda: stdin.readline().rstrip()

k, n = map(int, input().split())
nums = [ input() for _ in range(k) ]
nums += [ str(max(map(int, nums))) ] * ( n - len(nums) )

nums = sorted(nums, key=lambda x: int(("{:<016s}".format(str(x)))), reverse=True)
if all(num == "0" for num in nums): print(0); quit()

fixed = set()
while True:
    changed = False

    for i in range(n - 1):
        if (nums[i+1], nums[i]) not in fixed:

            numbers = nums.copy()
            numbers[i], numbers[i+1] = nums[i+1], nums[i] 

            previous_num = int("".join(nums))
            changed_num = int("".join(numbers))

            if changed_num > previous_num:
                nums = numbers
                changed = True

            fixed.add((nums[i+1], nums[i]))

    if changed == False: break

print("".join(nums))