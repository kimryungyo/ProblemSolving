n, *nums = open(0).read().split()
nums.sort(key=lambda x: int(x))
print("\n".join(nums))