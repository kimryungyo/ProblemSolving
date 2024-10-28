from collections import Counter
n, *nums = map(int, open(0).read().split())
counts = dict(Counter(nums))
graph = { num: [] for num in nums }

for num in nums:
    for other in nums:
        if other * 3 == num:
            graph[num].append(other)
        elif other == num * 2:
            graph[num].append(other)

def dfs(seq, uses):
    if len(seq) == n: print(*seq); quit()
    last = seq[-1]

    for next in graph[last]:
        if next in uses: continue

        new_seq = seq + (next,)
        new_uses = uses | {next}
        dfs(new_seq, new_uses)

for num in nums:
    dfs( (num,), {num} )