from sys import stdin
input = lambda: stdin.readline().rstrip()
from itertools import permutations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
perms = list(permutations(nums, M))
for perm in sorted(perms): print(' '.join(map(str, perm)))