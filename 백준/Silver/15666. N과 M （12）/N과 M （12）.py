from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
NUMS = sorted(set(map(int, input().split())))

def dfs(seq, i, M, NUMS):
    if len(seq) == M:
        for num in seq:
            print(num, end = " ")
        print()
        return
    
    for idx in range(i, len(NUMS)):
        new = seq + (NUMS[idx],)
        dfs(new, idx, M, NUMS)

dfs(tuple(), 0, M, NUMS)