n = int(input())
nums = sorted(input().split(), key=lambda x: int(("{:<010s}".format(x))), reverse=True)
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