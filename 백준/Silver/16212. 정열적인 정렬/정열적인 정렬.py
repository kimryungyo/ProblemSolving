n, *nums = map(int, open(0).read().split())
nums.sort()
print(" ".join(map(str, nums)))